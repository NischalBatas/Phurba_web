from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'hotel/index.html')

def rooms(request):
    room=Room.objects.all()
    context={
        "room":room
    }
    return render(request,'hotel/rooms.html',context)

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject = request.POST['subjects']
        messages = request.POST['messages']       

        data={
            'name':name,
            'email':email,
            'subject':subject,
            'message':messages
        }
        message='''
            New message:{}
            from:{}
        '''.format(data['message'],data['email'])

        send_mail(
        data['subject'],
        message,
        '',
        ['phurbatsheringsherpa333@gmail.com'],
        
        fail_silently=False,
        )
        return render(request, 'hotel/contact.html',{"messagen":"Message Sent"})
    else:
        return render(request, 'hotel/contact.html')

def about(request):
    team=Team.objects.all()
    context={
        'team':team
    }
    return render(request,'hotel/about.html',context)


def foods(request):
    food=Food.objects.all()
    context={
        "food":food
    }
    return render(request,'hotel/foods.html',context)