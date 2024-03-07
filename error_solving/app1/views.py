from django.shortcuts import render , HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request,'index.html')

def login(request):
  return render(request,'login.html')

def register(request):
  if request.method=='POST':
    uname=request.POST.get('uname')
    email=request.POST.get('email')
    pass1=request.POST.get('password1')
    pass2=request.POST.get('password2')
    my_user=User.objects.create_user(uname,email,pass1)
    my_user.save()
  return render(request,'register.html')


def home(request):
  return render(request,'home.html')


def about(request):
  return render(request,'about.html')


def contact(request):
  return render(request,'contact.html')