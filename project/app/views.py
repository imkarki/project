from django.shortcuts import render,redirect
from . models import Member
from . models import user

from django.contrib import auth,messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout



# Create your views here.
def home(request):
     return render(request,'home.html')


def registration(request):
    
        return render(request,'registration.html')
    

def login(request):
    return render(request,'login.html')

def thought(request):
    return render(request,'thought.html')

def register(request):
     if request.method=="POST":
          email=request.POST['email']
          password=request.POST['password']
          confirm=request.POST['repeat']
          mem=Member(email=email,password=password,confirm_password=confirm)
          mem.save()
          print("registration done successfully")
          return render(request,'thought.html')
     else:
          print("Register first")


def story(request):
     if request.method=="POST":
          title=request.POST['title']
          story=request.POST['story']
          quote=user(title=title,story=story)
          quote.save()
          return render(request,"header.html")
     else:
          print("write down first")


def m_view(request):
     email=request.POST.get('email')
     password=request.POST.get('password')
     user=authenticate(request,email=email,password=password)
     if user is not None:
          login(request,user)
          return redirect('/')
     else:
          messages.error(request,"invalid login details")
     return render(request,'login.html')
          
# def authen(request):
#      if request.method=='POST':
#           email=request.POST.get('email')
#           password=request.POST.get('password')
#           user=auth.authenticate(email=email,password=password)
#           if user is not None:
#                auth.login(request,user)
#                return redirect('/')
#           else:
#                messages.error(request,'Invalid login details')
#      return render(request,'login.html')


def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')

def ideas(request):
     data=user.objects.all()
     return render(request,'ideas.html',{'mem':data})
       
          
          # return render(request,'ideas.html',{'data':data})
     
# def ideas(request):
#      return render(request,'ideas.html')

def tracker(request):
     return render(request,'tracker.html')