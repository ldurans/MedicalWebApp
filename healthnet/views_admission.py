from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from healthnet.forms import AdmissionForm
from healthnet.models import Account, Admission, Action
from healthnet import logger
from healthnet import views

def admit_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_NURSE, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(
        request,
        {'form_button': "Admit"}
    )
    # Proceed with the rest of the view
    default = {}
    # Prefill some of the form values
    if 'hospital' not in request.POST and request.user.account.profile.prefHospital is not None:
        default['hospital'] = request.user.account.profile.prefHospital.pk
    if 'timestamp' not in request.POST:
        default['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    request.POST._mutable = True
    request.POST.update(default)
    form = AdmissionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            admission = form.generate()
            admission.save()
            logger.log(Action.ACTION_ADMISSION, 'Admitted Patient', request.user.account)
            form = AdmissionForm(default)  # Clean the form when the page is redisplayed
            form.clear_errors()
            request.session['alert_success'] = "Successfully admitted patient."  # Use session when passing data through a redirect
            return HttpResponseRedirect('/admission/list/')
    else:
        form._errors = {}
    template_data['form'] = form
    return render(request, 'healthnet/admission/admit.html', template_data)


def list_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_NURSE, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(request)
    # Proceed with the rest of the view
    if request.method == 'POST':
        if 'discharge' in request.POST and 'pk' in request.POST:
            pk = request.POST['pk']
            try:
                admission = Admission.objects.get(pk=pk)
                admission.active = False
                admission.discharged_timestamp = datetime.now()
                admission.save()
                logger.log(Action.ACTION_ADMISSION, 'Discharged Patient', request.user.account)
                template_data['alert_success'] = "The patient has been discharged."
            except Exception:
                template_data['alert_danger'] = "Unable to discharge the requested patient. Please try again later."
    template_data['query'] = Admission.objects.all()
    return render(request, 'healthnet/admission/list.html', template_data)