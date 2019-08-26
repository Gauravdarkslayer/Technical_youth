from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
from random import randint
from django.conf import settings
from django.db import connection
import smtplib


def home(request):
    return render(request,'colorlib-regform-7/login.html')


def login(request): # login form delivered
    if request.session.get('email'):
        error = "Already logged in"
        return HttpResponse('<h1>You are already logged in. Please logout first</h2>')
        # return render(request,"app1/afterlogin.html",{'error':error})
    else:
        form = Login()
        return render(request,'colorlib-regform-7/login.html',{'form':form})

def signup(request): # signup form delivered
    form = Signup()
    return render(request,'colorlib-regform-7/sign up.html')#,{'form':form})



class Signnedup(View): 
# Get data from forms
    def get(self,request):
            error = "Invalid method"
            form = Signup()
            return HttpResponse('<h1>Success in get</h1>')
            #render(request,"app1/signup.html",{'form':form,'error':error})

    def post(self,request):
        form = Signup(request.POST,request.FILES)

        if form.is_valid():
            mail = form.cleaned_data['email']            
                # print("got here")
            
            with connection.cursor() as cursor:
                current_user=cursor.execute("select *from user where emailid='{}'".format(mail))
                if current_user == 0:
                    p1 = form.cleaned_data['passwd']
                    p2 = form.cleaned_data['re_pass']
                    if p1 == p2:
                        dict = {
                        'username' : form.cleaned_data['name'],
                        'email' : form.cleaned_data['email'],
                        'password':form.cleaned_data['passwd'],
                        # 'pic' : form.cleaned_data['pic'],
                        }
                        
                        with connection.cursor() as cursor:
                            cmd="insert into user(emailid,username,password) values('{}','{}','{}')".format(dict['email'],dict['username'],dict['password'])
                            cursor.execute(cmd)                

                        return render(request,"colorlib-regform-7/login.html",{'dict':dict})
                    else:
                        error = "Password does not match...Try again"
                        return render(request,"colorlib-regform-7/sign up.html",{'error':error})
                else:
                    error = "User already exist..."
                    return render(request,"colorlib-regform-7/login.html",{'error':error})#'form':form,

        else:
                error = "Invalid Form"
                form = Signup()
                return HttpResponse('<h1>Invalid form</h1>')# return render(request,"app1/signup.html",{'form':form,'error':error})


def login1(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['passwor']
            with connection.cursor() as cursor:
                cursor.execute("select * from user where emailid='{}'".format(email))
                data = cursor.fetchone()
                print(data)
                if data == None:
                    error = "User doesn't exist"
                    return render(request,"colorlib-regform-7/login.html",{'error':error})
                if password == data[2]:
                    request.session['email'] = email
                    if data[10]=='N':
                        cursor.execute(f"update user set profilesetup='Y' where emailid='{email}'")
                        return render(request,"colorlib-regform-7/browseinterest.html")
                    else:
                        return render(request,"colorlib-regform-7/afterlogin.html")
                else:
                    error = "Password does not match..."
                    form = Login()
                    #return HttpResponse("<h1>Password doesnot matched</h1>")
                    return render(request,"colorlib-regform-7/login.html",{'error':error})#,{'form':form,'error':error})

        else:
            error = "Please Enter Valid Information"
            form = Login()
            #return HttpResponse("<h1>invalid form</h1>")
            return render(request,"colorlib-regform-7/login.html",{'error':error,'form':form})
    else:
        error = "invalid method"
        form = Login()
        #return HttpResponse("<h1>invalid method</h1>")
        return render(request,"colorlib-regform-7/login.html",{'error':error,'form':form})


def logout(request):
    del request.session['email']
    # return render(request,"app1/header.html")
    #return HttpResponse('<h1 style="color:cyan;background-color:black;">You are successfully logged out...</h1>')
    return render(request,"colorlib-regform-7/login.html")

# Function called in interest screen
def getinterest(request):
    
    def insert(interest):
        with connection.cursor() as cursor:
            mail=request.session['email'] #Getting current user email
            print(mail)
            cursor.execute("select id from user where emailid='{}'".format(mail))
            CURRENT_USER_ID=cursor.fetchone()
            print(CURRENT_USER_ID)
            cursor.execute("insert into getinterest (userid,interestid) values({},'{}')".format(*CURRENT_USER_ID,interest))
    INTEREST_PYTHON=request.POST.get('python') 
    #print("this is here",INTEREST_PYTHON)
    INTEREST_CPP=request.POST.get('c++') 
    #print("this is here",INTEREST_CPP)
    INTEREST_VFX=request.POST.get('vfx') 
    #print("this is here",INTEREST_VFX)
    INTEREST_JAVA=request.POST.get('java') 
    #print("this is here",INTEREST_JAVA)
    INTEREST_ANDROID=request.POST.get('android') 
    #print("this is here",INTEREST_ANDROID)
    INTEREST_PHP=request.POST.get('php') 
    #print("this is here",INTEREST_PHP)
    INTEREST_NODEjs=request.POST.get('node') 
    #print("this is here",INTEREST_NODEjs)
    INTEREST_GO=request.POST.get('go') 
    #print("this is here",INTEREST_GO)
    INTEREST_CSHARP=request.POST.get('csharp') 
    #print("this is here",INTEREST_CSHARP)
    if INTEREST_PYTHON:
        insert(INTEREST_PYTHON)
    if INTEREST_CPP:
        insert(INTEREST_CPP)
    if INTEREST_VFX:
        insert(INTEREST_VFX)
    if INTEREST_JAVA:
        insert(INTEREST_JAVA)
    if INTEREST_ANDROID:
        insert(INTEREST_ANDROID)
    if INTEREST_PHP:
        insert(INTEREST_PHP)
    if INTEREST_NODEjs:
        insert(INTEREST_NODEjs)
    if INTEREST_GO:
        insert(INTEREST_GO)
    if INTEREST_CSHARP:
        insert(INTEREST_CSHARP)
    return render(request,'allblog.html')

    # ml = request.POST.get('ML')
    # print("This is 2nd item",ml)
myotp=""
def render_forgot_template(request):
    return render(request,'colorlib-regform-7/forgot.html')

otp=randint(1000,9999)
myemail=""

def forgots(request):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('www.gaurav10bhojwani@gmail.com','inuajyeavvhhcxfo')
    subject="otp for technical youth"
    body="DO NOT SHARE THIS OTP WITH ANYONE"+" "+str(otp)
    msg=f'subject: {subject}\n\n{body}'
    global myemail
    server.sendmail(
            'www.gaurav10bhojwani@gmail.com',
             request.POST.get('email'),
            # 'gaurav10me@gmail.com',
            msg
        )   
    myemail=request.POST.get('email')    
    print("sent successfully")
    server.quit()
    return render(request,'colorlib-regform-7/enterotp.html')

def getotp(request):
    if str(otp) == request.POST.get('otp'):
        # return HttpResponse("OK OTP matched")
        return render(request,'colorlib-regform-7/newpassword.html')
    else:
        return HttpResponse("Otp does'nt match, Please try again later")

def updatePassword(request):
    p1=request.POST.get('newpass')
    p2=request.POST.get('confirmpass')
    if p1==p2:
        with connection.cursor() as cursor:
            global myemail
            cursor.execute("UPDATE user SET password = '{}' where emailid = '{}'".format(p1,myemail))
            return HttpResponse("Password changed successfully, you can now return to login page")
            return render(request,'colorlib-regform-7/login.html')
    else:
        return HttpResponse('new password and confirm password does\'nt matched')        





















    