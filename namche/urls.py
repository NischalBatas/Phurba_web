from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name="index"),
    path('rooms',views.rooms,name="rooms"),
    path('contact',views.contact,name='contacts'),
    path('about',views.about,name="about"),
    path('foods',views.foods,name="foods"),
    path('addfood',views.addfood,name="addfood"),
    path('updatefood/<food_id>',views.updatefood,name="updatefood"),
    path('deletefood/<food_id>',views.deletefood,name="deletefood"),
    path('addroom',views.addroom,name="addroom"),
    path('updateroom/<room_id>',views.updateroom,name="updateroom"),
    path('deleteroom/<room_id>',views.deleteroom,name="deleteroom"),

    path('booking',views.booking,name="booking"),
    path('addbooking',views.addbooking,name="addbooking"),
    path('dashboard',views.dashboard,name="dashboard"),



]


urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)