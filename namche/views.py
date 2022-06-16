from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    room=Room.objects.all()[:6]
    context={
        "room":room
    }
    return render(request,'hotel/index.html',context)

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
        return render(request, 'hotel/contact.html',{"messagen":"Message Sent","name":name})
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

def addfood(request):
    if request.method=="POST":
        form=FoodForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"New Food Added")
            return redirect('foods')
    else:
        form=FoodForm()
    context={
        "form":form
    }
    return render(request,'hotel/crud/addfood.html',context)

def updatefood(request,food_id):
    food=Food.objects.get(pk=food_id)
    form=FoodForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        messages.info(request, 'Menu Updated Successfully')
        return redirect('foods')

    context={
        'form':form
    }
    return render(request,'hotel/crud/updatefood.html',context)

def deletefood(request,food_id):
    food=Food.objects.get(pk=food_id)
    food.delete()
    messages.error(request, 'Room Delete Successfully')
    return redirect('foods')


def foods(request):
    food=Food.objects.all()
    context={
        "food":food
    }
    return render(request,'hotel/foods.html',context)

def addroom(request):
    if request.method=="POST":
        form=RoomForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"New room Added")
            return redirect('rooms')
    else:
        form=RoomForm()
    context={
        "form":form
    }
    return render(request,'hotel/crud/addroom.html',context)

def updateroom(request,room_id):
    room=Room.objects.get(pk=room_id)
    form=RoomForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        messages.info(request, 'Update Room Successfully')
        return redirect('rooms')

    context={
        'form':form
    }
    return render(request,'hotel/crud/updateroom.html',context)

def deleteroom(request,room_id):
    room=Room.objects.get(pk=room_id)
    room.delete()
    messages.error(request, 'Room Delete Successfully')
    return redirect('rooms')

def booking(request):
    booking=Booking.objects.all()
    context={
        "booking":booking
    }
    return render(request,'hotel/booking.html',context)

def addbooking(request):
    if request.method=="POST":
        form=BookingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking Successfully')
            return redirect('addbooking')
    else:
        form=BookingForm()
    context={
        "form":form
    }

    return render(request,'hotel/crud/addbooking.html',context)

def dashboard(request):
    return render(request,'auth/dashboard.html')
