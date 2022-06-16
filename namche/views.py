from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import *

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
        return redirect('foods')

    context={
        'form':form
    }
    return render(request,'hotel/crud/updatefood.html',context)

def deletefood(request,food_id):
    food=Food.objects.get(pk=food_id)
    food.delete()
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
        return redirect('rooms')

    context={
        'form':form
    }
    return render(request,'hotel/crud/updateroom.html',context)

def deleteroom(request,room_id):
    room=Room.objects.get(pk=room_id)
    room.delete()
    return redirect('rooms')

def booking(request):
    booking=Booking.objects.all()
    context={
        "booking":booking
    }
    return render(request,'hotel/booking.html',context)

def addbooking(request):
    user=request.user
    if request.method=="POST":
        print(request.POST["username"])
        cu_username=request.POST['username']
        cu_email=request.POST['semail']
        cu_phone=request.POST['phone']
        cu_sphone=request.POST['sphone']
        cu_message=request.POST['message']
        adults=request.POST['adults']
        rname=request.POST['roomname']
        datefrom=request.POST['datefrom']
        dateto=request.POST['dateto']



        ccontact=Booking(uname=cu_username,email=cu_email,phone=cu_phone,s_phone=cu_sphone,message=cu_message,roomname=rname,adult=adults,date_from=datefrom,date_to=dateto)
        ccontact.save()
        messages.success(request, 'Message Successfully sent')

    return render(request,'hotel/crud/addbooking.html',{'user':user})

def dashboard(request):
    return render(request,'auth/dashboard.html')
