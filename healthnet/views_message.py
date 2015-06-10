from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect

from healthnet.models import Message
from healthnet import logger
from healthnet.forms import MessageForm
from healthnet.models import Action, Account
from healthnet import views
from healthnet.views import sanitize_js
from healthnet import message


def list_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(request)
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(request)
    # Proceed with the rest of the view
    # Parse search sorting
    message.parse_message_archive(request, template_data)
    template_data['messages'] = Message.objects.filter(Q(target=request.user.account) | Q(sender=request.user.account))
    template_data['account'] = sanitize_js(request.user.account.profile.__str__())
    return render(request, 'healthnet/message/list.html', template_data)


def new_view(request):
    # Authentication check.
    authentication_result = views.authentication_check(request)
    if authentication_result is not None: return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(
        request,
        {'form_button': "Send Message"}
    )
    # Proceed with the rest of the view
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.generate(request.user.account)
            message.save()
            logger.log(Action.ACTION_MESSAGE, 'Message sent', request.user.account)
            request.session['alert_success'] = "Successfully sent your message!"
            return HttpResponseRedirect('/message/list/')
    else:
        # Validation Check. Make sure a message exists for the given pk.
        default = {}
        if 'pk' in request.GET:
            pk = request.GET['pk']
            try:
                account = Account.objects.get(pk=pk)
                default['target'] = pk
            except Exception:
                template_data['alert_danger'] = "We couldn't find the person you're replying to. Please try again.."

        form = MessageForm(default)
        form.clear_errors()
    template_data['form'] = form
    return render(request, 'healthnet/message/new.html', template_data)