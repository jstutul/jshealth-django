from django.urls import path
from service import views
urlpatterns=[
    path('',views.index,name='home'),
    path('contact',views.contactus,name='contact'),
    path('services',views.services,name='services'),
    path('services/<int:id>',views.signleservice,name='singleservice'),
    path('about',views.about,name='about'),
    path('login',views.loginView,name='loginview'),
    path('signup',views.registerView,name='signup'),
    path('logout',views.Logoutview,name='logout'),



]