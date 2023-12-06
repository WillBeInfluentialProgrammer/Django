from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='aboutus'),
    path('contact/',views.contact, name='contactus'),
    path('simple/',views.simpleForm, name='form'),

]