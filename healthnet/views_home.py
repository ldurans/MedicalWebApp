from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from healthnet.forms import LoginForm, AccountRegisterForm, PatientRegisterForm
from healthnet.models import Account, Action
from healthnet import views
from healthnet import logger


def setup_view(request):
    if Account.objects.all().count() > 0:
        request.session['alert_success'] = "Setup has already been completed."
        return HttpResponseRedirect('/')
    # Get the template data from the session
    template_data = views.parse_session(request, {'form_button': "Register"})
    # Proceed with the rest of the view
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            views.register_user(
                form.cleaned_data['email'],
                form.cleaned_data['password_first'],
                form.cleaned_data['firstname'],
                form.cleaned_data['lastname'],
                Account.ACCOUNT_ADMIN
            )
            user = authenticate(
                username=form.cleaned_data['email'].lower(),  # Make sure it's lowercase
                password=form.cleaned_data['password_first']
            )
            logger.log(Action.ACTION_ACCOUNT, "Account login", user.account)
            login(request, user)
            request.session['alert_success'] = "Successfully setup HealthNet's primary admin account."
            return HttpResponseRedirect('/profile/')
    else:
        form = AccountRegisterForm()
    template_data['form'] = form
    return render(request, 'healthnet/setup.html', template_data)


def logout_view(request):
    if request.user.is_authenticated():
        logger.log(Action.ACTION_ACCOUNT, "Account logout", request.user.account)
    # Django deletes the session on logout, so we need to preserve any alerts currently waiting to be displayed
    saved_data = {}
    if request.session.has_key('alert_success'):
        saved_data['alert_success'] = request.session['alert_success']
    else:
        saved_data['alert_success'] = "You have successfully logged out."
    if request.session.has_key('alert_danger'):
        saved_data['alert_danger'] = request.session['alert_danger']
    logout(request)
    if 'alert_success' in saved_data:
        request.session['alert_success'] = saved_data['alert_success']
    if 'alert_danger' in saved_data:
        request.session['alert_danger'] = saved_data['alert_danger']
    return HttpResponseRedirect('/')


def login_view(request):
    # Authentication check. Users currently logged in cannot view this page.
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    elif Account.objects.all().count() == 0:
        return HttpResponseRedirect('/setup/')
    # Get the template data from the session
    template_data = views.parse_session(request, {'form_button': "Login"})
    # Proceed with the rest of the view
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'].lower(),  # Make sure it's lowercase
                password=form.cleaned_data['password']
            )
            login(request, user)
            logger.log(Action.ACTION_ACCOUNT, "Account login", request.user.account)
            request.session['alert_success'] = "Successfully logged into HealthNet."
            return HttpResponseRedirect('/profile/')
    else:
        form = LoginForm()
    template_data['form'] = form
    return render(request, 'healthnet/login.html', template_data)


def register_view(request):
    # Authentication check. Users logged in cannot view this page.
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    elif Account.objects.all().count() == 0:
        return HttpResponseRedirect('/setup/')
    # Get the template data from the session
    template_data = views.parse_session(request, {'form_button': "Register"})
    # Proceed with the rest of the view
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            views.register_user(
                form.cleaned_data['email'],
                form.cleaned_data['password_first'],
                form.cleaned_data['firstname'],
                form.cleaned_data['lastname'],
                Account.ACCOUNT_PATIENT,
                form.cleaned_data['insurance']
            )
            user = authenticate(
                username=form.cleaned_data['email'].lower(),  # Make sure it's lowercase
                password=form.cleaned_data['password_first']
            )
            logger.log(Action.ACTION_ACCOUNT, "Account login", user.account)
            login(request, user)
            request.session['alert_success'] = "Successfully registered with HealthNet."
            return HttpResponseRedirect('/profile/')
    else:
        form = PatientRegisterForm()
    template_data['form'] = form
    return render(request, 'healthnet/register.html', template_data)


def error_denied_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(request)
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(request)
    # Proceed with the rest of the view
    return render(request, 'healthnet/error/denied.html', template_data)