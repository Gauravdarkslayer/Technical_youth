from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
# Create your views here.

# def index(request):
#     return render(request,'app1/header.html')

def home(request):
    return render(request,'colorlib-regform-7/login.html')


def login(request):
    form = Login()
    return render(request,'colorlib-regform-7/login.html',{'form':form})

def signup(request):
    form = Signup()
    return render(request,'colorlib-regform-7/signup.html',{'form':form})

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
