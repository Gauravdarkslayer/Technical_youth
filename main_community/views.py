from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
from pymongo import *
from .models import AddUser
from django.conf import settings

# Create your views here
# def index(request):
#     return render(request,'app1/header.html')

def home(request):
    return render(request,'colorlib-regform-7/login.html')


def login(request):
    form = Login()
    return render(request,'colorlib-regform-7/login.html',{'form':form})

def signup(request):
    form = Signup()
    return render(request,'colorlib-regform-7/sign up.html')#,{'form':form})



#mongodb Database connection
#MONGODB_URI = 'mongodb://<Gaurav>:<gaurav123>@ds253567.mlab.com:53567/connect_login_signup'
"""MONGODB_URI   = settings.DATABASES['default']['HOST']
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.connect_login_signup
user_records = db.userdata
print('connected successfully')
user_records.insert_one({'name':'bro','email':'asd@o.com','passwd':'123'})
user_records.save()
print('insertedddddddddddddddddddddddddddd')"""
# print('added successfully')
# def pushRecord(record):
#     user_records.insert_one(record)

class Signnedup(View):
# Get data from forms
    def get(self,request):
            error = "Invalid method"
            form = Signup()
            return HttpResponse('<h1>Success</h1>')#render(request,"app1/signup.html",{'form':form,'error':error})
    def post(self,request):
        print('called POST function')
        form = Signup(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print('after calling')
            mail = form.cleaned_data['email']

            try:
                 # data=request.POST.get(mail='email')
                data=AddUser.objects.get(email=mail)
                 #print(data)

            except AddUser.DoesNotExist as e:
                print('in exist')
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
                    #print('inserting')
                    #user_records.insert_one(dict)
                    # pushRecord(dict)
                    # new_user = AddUser.objects.create(**dict)
                    print('inserted')
                    #user_records.save()
                    #print('saved')
                    return HttpResponse('<h1>Success</h1>')#render(request,"app1/data.html",{'dict':dict})
                else:
                    error = "Password does not match...Try again"
                    form = Signup()
                    return HttpResponse('<h1>password not matched</h1>')# return render(request,"app1/signup.html",{'form':form,'error':error})
            else:
                error = "User already exist..."
                form = Signup()
                return HttpResponse('<h1>user already exist</h1>')# return render(request,"app1/signup.html",{'form':form,'error':error})

        else:
                error = "Invalid Form"
                form = Signup()
                return HttpResponse('<h1>Invalid form</h1>')# return render(request,"app1/signup.html",{'form':form,'error':error})
# class Signnedup(View):
#     def get(self,request):
#         error = 'Invalid method'
#         form=Signup()
#         return render(request,'app1/signup1/',{'form':form})
#
#     def signup(self,request):
#         form=Signup(request.POST,request.FILES)
#         if form.is_valid():
#             p1 = form.cleaned_data()
#         else:
#             error = 'Invalid password try agian'
#             form=Signup()
#             return render(request,'app1/signup.html',{'form':form,'error':error})
