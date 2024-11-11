from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.signup_page,name='signup'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department')
]