from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
# from pymongo import *
from .models import AddUser
from django.conf import settings


# Create your views here
# def index(request):
#     return render(request,'app1/header.html')

def home(request):
    return render(request,'colorlib-regform-7/login.html')


def login(request):
    if request.session.get('email'):
        error = "Already logged in"
        return HttpResponse('<h1>You are already logged in. Please logout first</h2>')
        # return render(request,"app1/afterlogin.html",{'error':error})
    else:
        form = Login()
        return render(request,'colorlib-regform-7/login.html',{'form':form})

def signup(request):
    form = Signup()
    return render(request,'colorlib-regform-7/sign up.html')#,{'form':form})



class Signnedup(View):
# Get data from forms
    def get(self,request):
            error = "Invalid method"
            form = Signup()
            return HttpResponse('<h1>Success in get</h1>')#render(request,"app1/signup.html",{'form':form,'error':error})

    def post(self,request):
        form = Signup(request.POST,request.FILES)

        if form.is_valid():
            print('after calling')
            mail = form.cleaned_data['email']

            try:
                data=AddUser.objects.get(email=mail)

            except AddUser.DoesNotExist as e:
                p1 = form.cleaned_data['passwd']
                p2 = form.cleaned_data['re_pass']
                if p1 == p2:
                    dict = {
                    'username' : form.cleaned_data['name'],
                    'email' : form.cleaned_data['email'],
                    'password':form.cleaned_data['passwd'],
                    # 'pic' : form.cleaned_data['pic'],
                    }

                    new_obj = AddUser.objects.create(**dict)
                    new_obj.save()
                    # return HttpResponse('<h1>Success, Now you can login</h1>')

                    return render(request,"colorlib-regform-7/login.html",{'dict':dict})
                else:
                    error = "Password does not match...Try again"
                    form = Signup()
                    return HttpResponse('<h1>password not matched</h1>')# return render(request,"app1/signup.html",{'form':form,'error':error})
            else:
                error = "User already exist..."
                form = Signup()
                # return HttpResponse('<h1>user already exist</h1>')
                return render(request,"colorlib-regform-7/login.html",{'error':error})#'form':form,

        else:
                error = "Invalid Form"
                form = Signup()
                return HttpResponse('<h1>Invalid form</h1>')# return render(request,"app1/signup.html",{'form':form,'error':error})


def login1(request):
    form = Login(request.POST)
    if request.method == "POST":
        # print(form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['passwor']
            user = AddUser.objects.get(email=email)
            if password == user.password:
                request.session['email'] = email
                return render(request,"colorlib-regform-7/afterlogin.html")
                # return HttpResponse("<h1>success</h1>")
            else:
                error = "Password does not match..."
                form = Login()
                return HttpResponse("<h1>Password doesnot matched</h1>")
                # return render(request,"colorlib-regform-7/login.html",{'form':form,'error':error})

        else:
            error = "invalid form"
            form = Login()
            return HttpResponse("<h1>invalid form</h1>")
            # return render(request,"colorlib-regform-7/login.html",{'error':error,'form':form})
    else:
        error = "invalid method"
        form = Login()
        return HttpResponse("<h1>invalid method</h1>")
        # return render(request,"colorlib-regform-7/login.html",{'error':error,'form':form})


def logout(request):
    del request.session['email']
    # return render(request,"app1/header.html")
    return HttpResponse('<h1 style="color:cyan;background-color:black;">You are successfully logged out...</h1>')
