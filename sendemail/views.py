from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from .forms import NameForm, AbcForm
from . models import Abc

# Create your views here.
def sendemail(request, pk=None):
    subject = 'Thank you for registering to our site'
    # message = ' it  means a world to us '
    # text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    from_email = 'testing@local.com'
    context = {
            'news': 'We have good news!'
        }
    # recipient_list = ['receiver@gmail.com',]
    to = ['receiver@gmail.com',]
    # if subject and message and email_from:
    if subject and html_content and from_email:
        try:
            msg_html = render_to_string('email.html',context)
            msg = EmailMessage(subject=subject, body=msg_html, from_email=from_email, to=to)
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            # msg = EmailMultiAlternatives(subject, html_content, email_from, to)
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            # send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            # send_mail(subject, message, from_email, ['admin@example.com'])
            Abc.objects.filter(pk=pk).update(flagcalc=1)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        # return HttpResponse('redirect to a new page')
        return HttpResponseRedirect('%s%s' % ('/sendemail/cc/',pk))
        # return "%s - %s " % (self.preproject, status_psa_1)
    # return '' 


def index(request, paramm=None):
    if paramm:
        a = Abc.objects.all()
        m = paramm
    else:
        a = Abc.objects.all()
        m = ''
    
    return render(request, 'table.html', {
            'a':a,
            'm':m,
    })
    # return HttpResponse('redirect to a new page')

# def sendSimpleEmail(request,emailto):
#    res = send_mail("hello paul", "simple send email", "aah@simple.com", [emailto])
#    return HttpResponse('%s'%res)

# def form_create(request):
#     if request.method == 'POST':
#         form = AbcForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('blog_create')
#             return HttpResponse('form created')
#     else:
#         form = AbcForm()
#     return render(request,
#                   'create_form.html',
#                   {
#                       'form': form
#                   })

# def sendemailform(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = AbcForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/sendemail/form#')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = AbcForm()

#     return render(request, 'sendemailform.html', {'form': form})
