from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name="register"),
    path('thought/',views.thought,name="thought"),
    path('story/',views.story,name='story'),
    path('m_view/',views.m_view,name='m_view'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name='contact'),
    path('ideas/',views.ideas,name='ideas'),
    path('tracker/',views.tracker,name='tracker'),
    path('logout/', LogoutView.as_view(next_page='/registration/'), name='logout'),
    # path('message/',views.message,name='message')
    
    # path('authen/',views.authen,name='authen')

]