from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q

from healthnet.forms import AppointmentForm
from healthnet.models import Account, Appointment, Action
from healthnet import views
from healthnet import appointment
from healthnet import logger
from healthnet import message


def list_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_PATIENT, Account.ACCOUNT_NURSE, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(request)
    # Proceed with the rest of the view
    appointment.parse_appointment_cancel(request, template_data)  # Parse appointment cancelling
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        template_data['query'] = Appointment.objects.filter(patient=request.user.account)
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        template_data['query'] = Appointment.objects.filter(doctor=request.user.account)
    else:
        template_data['query'] = Appointment.objects.all()
    return render(request, 'healthnet/appointment/list.html', template_data)


def calendar_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_PATIENT, Account.ACCOUNT_NURSE, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(request)
    # Proceed with the rest of the view
    # Parse search sorting
    appointment.parse_appointment_cancel(request, template_data)  # Parse appointment cancelling
    template_data['events'] = appointment.parse_appointments(request)  # Build list of appointments
    return render(request, 'healthnet/appointment/calendar.html', template_data)


def update_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(request, None, ['pk'])
    if authentication_result is not None: return authentication_result
    # Validation Check. Make sure an appointment exists for the given pk.
    pk = request.GET['pk']
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Exception:
        request.session['alert_danger'] = "The requested appointment does not exist."
        return HttpResponseRedirect('/error/denied/')
    # Get the template data from the session
    template_data = views.parse_session(
        request,
        {
            'form_button': "Update Appointment",
            'form_action': "?pk=" + pk,
            'appointment': appointment
        }
    )
    # Proceed with the rest of the view
    request.POST._mutable = True
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        request.POST['patient'] = request.user.account.pk
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        request.POST['doctor'] = request.user.account.pk
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.assign(appointment)
            if Appointment.objects.filter(
                    ~Q(pk=appointment.pk),
                    Q(status="Active"),
                    Q(doctor=appointment.doctor) | Q(patient=appointment.patient),
                    Q(startTime__range=(appointment.startTime, appointment.endTime)) | Q(endTime__range=(appointment.startTime, appointment.endTime))).count():
                form.mark_error('startTime', 'That time conflicts with another appointment.')
                form.mark_error('endTime', 'That time conflicts with another appointment.')
            else:
                appointment.save()
                logger.log(Action.ACTION_APPOINTMENT, 'Appointment updated', request.user.account)
                template_data['alert_success'] = "The appointment has been updated!"
                template_data['form'] = form
                if request.user.account.role == Account.ACCOUNT_PATIENT:
                    message.send_appointment_update(request, appointment, appointment.doctor)
                elif request.user.account.role == Account.ACCOUNT_DOCTOR:
                    message.send_appointment_update(request, appointment, appointment.patient)
                else:
                    message.send_appointment_update(request, appointment, appointment.doctor)
                    message.send_appointment_update(request, appointment, appointment.patient)

    else:
        form = AppointmentForm(appointment.get_populated_fields())
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        form.disable_field('patient')
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        form.disable_field('doctor')
    template_data['form'] = form
    return render(request, 'healthnet/appointment/update.html', template_data)


def create_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_PATIENT, Account.ACCOUNT_NURSE, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(request, {'form_button': "Create"})
    # Proceed with the rest of the view
    default = {}
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        default['patient'] = request.user.account.pk
        if 'doctor' not in request.POST and request.user.account.profile.primaryCareDoctor is not None:
            default['doctor'] = request.user.account.profile.primaryCareDoctor.pk
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        default['doctor'] = request.user.account.pk
    if 'hospital' not in request.POST and request.user.account.profile.prefHospital is not None:
        default['hospital'] = request.user.account.profile.prefHospital.pk
    request.POST._mutable = True
    request.POST.update(default)
    form = AppointmentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            appointment = form.generate()
            if Appointment.objects.filter(
                    Q(status="Active"),
                    Q(doctor=appointment.doctor) | Q(patient=appointment.patient),
                    Q(startTime__range=(appointment.startTime, appointment.endTime)) | Q(endTime__range=(appointment.startTime, appointment.endTime))).count():
                form.mark_error('startTime', 'That time conflicts with another appointment.')
                form.mark_error('endTime', 'That time conflicts with another appointment.')
            else:
                appointment.save()
                logger.log(Action.ACTION_APPOINTMENT, 'Appointment created', request.user.account)
                form = AppointmentForm(default)  # Clean the form when the page is redisplayed
                form._errors = {}
                request.session['alert_success'] = "Successfully created your appointment!"
                if request.user.account.role == Account.ACCOUNT_PATIENT:
                    message.send_appointment_create(request, appointment, appointment.doctor)
                elif request.user.account.role == Account.ACCOUNT_DOCTOR:
                    message.send_appointment_create(request, appointment, appointment.patient)
                else:
                    message.send_appointment_create(request, appointment, appointment.doctor)
                    message.send_appointment_create(request, appointment, appointment.patient)
                return HttpResponseRedirect('/appointment/list/')
    else:
        form._errors = {}
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        form.disable_field('patient')
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        form.disable_field('doctor')
    template_data['form'] = form
    return render(request, 'healthnet/appointment/create.html', template_data)