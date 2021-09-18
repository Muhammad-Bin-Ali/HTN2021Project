from os import name
from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from .models import data
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def inpt(request):
    if inpt == "get":
        lister(request)
    else:
        insert(request)

def lister(request):
	context = data.objects.all() # Collect all records from table 
	return render(request,'App/main.html',{'context':context})
    
def insert(request):
	
    dt = data(name='name', description= 'description', Subscriptions='Subscriptions', payment_due='payment_due', payment_amount='payment_amount', image='image')
    dt.save()
    return redirect('/')

  ##  def insert(request):
   ## member = Member(firstname=request.POST&#91;'firstname'], lastname=request.POST&#91;'lastname'], address=request.POST&#91;'address'])
    ## member.save()
     ## return redirect('/')

#CHEESE OP TBH stfu

def email(request):
    
    subject = 'Subscriptions Being Renewed'#CHEESE OP TBH
    message = 'Reminder that your subscriptions will renew soon, pease review them for cancellation or continued renewal.'#CHEESE OP TBH
    email_from = settings.EMAIL_HOST_USER#CHEESE OP TBH
    #We have to append the user email to this array or just set it equal to#CHEESE OP TBH
    recipient_list = ['1bandisre@gmail.com',]#CHEESE OP TBH
    send_mail( subject, message, email_from, recipient_list, fail_silently = False)
    
    return redirect ('/')
    