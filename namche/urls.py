from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name="index"),
    path('rooms',views.rooms,name="rooms"),
    path('contact',views.contact,name='contacts'),
    path('about',views.about,name="about"),
    path('foods',views.foods,name="foods")


]


urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)