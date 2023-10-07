from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect("register")
        return redirect('/')


    return render (request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request,'form.html')
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     dob = request.POST['dob']
    #     age = request.POST['age']
    #     gender = request.POST['gender']
    #     pno = request.POST['pno']
    #     email = request.POST['email']
    #     course = request.POST['course']
    #     pup = request.POST['pup']
    #     address = request.POST['address']
    #     mat = request.POST['mat']
    #     if User.objects.filter(email=email).exists():
    #         messages.info(request, "email taken")
    #         return redirect('form.html')
    #     else:
    #         myuser= User.objects.create_user(username=username,gender=gender, dob=dob,age=age,pup=pup,mat=mat,
    #                                             pno=pno, email=email,course=course, address=address)
    #         myuser.save();
    #         return redirect('formf.html')


def formf(request):
    return render(request,'formf.html')

