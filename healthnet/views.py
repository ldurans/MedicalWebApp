from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from healthnet.models import Account, Profile, Action, MedicalInfo
from healthnet import logger


def authentication_check(request, required_roles=None, required_GET=None):
    """
    :param request: The page request
    :param required_roles: The role values of the users allowed to view the page
    :param required_GET: The GET values that the page needs to function properly
    :return: A redirect request if there's a problem, None otherwise
    """
    # Authentication check. Users not logged in cannot view this page.
    if not request.user.is_authenticated():
        request.session['alert_danger'] = "You must be logged into HealthNet to view that page."
        return HttpResponseRedirect('/')
    # Sanity check. Users without accounts cannot interact with HealthNet
    try:
        request.user.account
    except ObjectDoesNotExist:
        request.session['alert_danger'] = "Your account was not properly created, please try a different account."
        return HttpResponseRedirect('/logout/')
    # Permission Check.
    if required_roles and request.user.account.role not in required_roles:
        request.session['alert_danger'] = "You don't have permission to view that page."
        return HttpResponseRedirect('/error/denied/')
    # Validation Check. Make sure this page has any required GET keys.
    if required_GET:
        for key in required_GET:
            if key not in request.GET:
                request.session['alert_danger'] = "Looks like you tried to use a malformed URL."
                return HttpResponseRedirect('/error/denied/')


def parse_session(request, template_data=None):
    """
    Checks the session for any alert data. If there is alert data, it added to the given template data.
    :param request: The request to check session data for
    :param template_data: The dictionary to update
    :return: The updated dictionary
    """
    if template_data is None:
        template_data = {}
    if request.session.has_key('alert_success'):
        template_data['alert_success'] = request.session.get('alert_success')
        del request.session['alert_success']
    if request.session.has_key('alert_danger'):
        template_data['alert_danger'] = request.session.get('alert_danger')
        del request.session['alert_danger']
    return template_data


def register_user(email, password, firstname, lastname, role, insurance=""):
    user = User.objects.create_user(
        email.lower(),
        email.lower(),
        password
    )
    profile = Profile(
        firstname=firstname,
        lastname=lastname,
        insurance=insurance,
    )
    profile.save()
    account = Account(
        role=role,
        profile=profile,
        user=user
    )
    account.save()
    medical_info = MedicalInfo(
        account=account
    )
    medical_info.save()
    logger.log(Action.ACTION_ACCOUNT, "Account registered", account)
    return user

def sanitize_js(string):
    return string.replace("\\", "\\\\").replace("'", "\\'")