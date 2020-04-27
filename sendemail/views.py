from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm, AbcForm
from . models import Abc

# Create your views here.
def sendemail(request, pk=None):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    if subject and message and email_from:
        try:
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            # send_mail(subject, message, from_email, ['admin@example.com'])
            Abc.objects.filter(pk=pk).update(flagcalc=1)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        # return HttpResponse('redirect to a new page')
        return HttpResponseRedirect('%s%s' % ('/sendemail/cc/',pk))
        # return "%s - %s " % (self.preproject, status_psa_1)
    # return '' 

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "simple send email", "aah@simple.com", [emailto])
   return HttpResponse('%s'%res)

def form_create(request):
    if request.method == 'POST':
        form = AbcForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('blog_create')
            return HttpResponse('form created')
    else:
        form = AbcForm()
    return render(request,
                  'create_form.html',
                  {
                      'form': form
                  })

def sendemailform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AbcForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/sendemail/form#')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AbcForm()

    return render(request, 'sendemailform.html', {'form': form})

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

