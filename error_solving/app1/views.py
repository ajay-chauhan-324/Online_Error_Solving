from django.shortcuts import render , HttpResponse,redirect
from django.contrib.auth.models import User
from app1.models import User


# Create your views here.
def index(request):
  return render(request,'index.html')

def login(request):
  return render(request,'login.html')

def register(request):
  if request.method=='POST':
    uname=request.POST.get('uname')
    email=request.POST.get('email')
    pass1=request.POST.get('pass1')
    
    my_user=User(uname=uname,email=email,pass1=pass1)
    my_user.save()
    print(my_user)
    return redirect('/')
  else:
    return render(request,'register.html')


def home(request):
  return render(request,'home.html')


def about(request):
  return render(request,'about.html')


def contact(request):
  return render(request,'contact.html')