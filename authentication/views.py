from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,"authentication/index.html")


def signup(request):

    if request.method == "POST":
        userName = request.POST['username']
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        password_1 = request.POST['pass1']
        password_2 = request.POST['pass2']

        myuser = User.objects.create_user(userName,email,password_1)
        myuser.first_name = firstName
        myuser.last_name = lastName

        myuser.save()

        messages.success(request, "Your Account has been Created...")
        return redirect('signin')


    return render(request,"authentication/signup.html")


def signin(request):
    return render(request,"authentication/signin.html")


def signout(request):
    pass