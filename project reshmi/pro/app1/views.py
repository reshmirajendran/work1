# from django.shortcuts import render

# from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse
# from django.contrib.auth import authenticate,login,logout

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.contrib import messages





def base(request):
    return render(request,'base.html')
# 



def form1(request):
     if (request.method =='POST'):
        ph=request.POST['phoneno']
        em=request.POST['email']
        cn=request.POST['coursename']
        current_user = request.user

        if courseregistration.objects.filter(email=em).exists():
             messages.error(request,'email id already exist')
             return redirect('form1')
        
        elif courseregistration.objects.filter(coursename=cn).exists():
             messages.error(request,'already registered')
             return redirect('form1')
        
        elif courseregistration.objects.filter(phoneno=ph).exists():
             messages.error(request,'phone number already exist')
             return redirect('form1')
        
        else:
            o=courseregistration.objects.create(phoneno=ph,email=em,coursename=cn,user_id=current_user.id)
            o.save()
            messages.success(request,'successfully submitted')
     return render(request,'form1.html') 


def about(request):
    return render(request,'about.html')
def course(request):
#   
    return render(request,'course.html')
def contact(request):
    return render(request,'contact.html')    



def signup(request):
     if(request.method =='POST'):
            username=request.POST['username']
            email=request.POST['email']
            password1=request.POST['password1']
            #Check if user already exists
            if User.objects.filter(username=username).exists():
                    messages.error(request,'Username already exists')
            if User.objects.filter(email=email).exists():
                    messages.error(request,'EmailId already exists')
                    return redirect('signup')
            myuser=User.objects.create_user(username,email,password1)
            myuser.save()
            return base(request)
     return render(request,'signup.html')

def user_login(request):
    if(request.method =='POST'):
            name=request.POST['n']
            password=request.POST['p']
            user = authenticate(username=name,password=password)
            if user:
                login(request,user)
                return base(request)
            else:
               messages.error(request,'invalid user')
               return redirect('login')
    return render(request,'login.html' )    
def logout1(request):
    logout(request)
    return user_login(request)    