from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.forms import Form
# Create your views here.

def all_posts(request):
    with connection.cursor() as cursor:
        cursor.execute("select post from posts")
        blogs=cursor.fetchall()
        b=[]
        for var in blogs:
            dict={
                'post':var
            }
            b.append(var)
        return render(request,"allblog.html",{'all':b})    

def question_post(request):
   return render(request,'question_post.html')

def postnewquestion(request):
    question=request.POST.get("question_field")
    email=request.session['email']

    with connection.cursor() as cursor:
        qry2=f"select id from user where emailid='{email}'"
        cursor.execute(qry2)
        id=(cursor.fetchone())
        qry="insert into posts (post,userid) values ('{}','{}')".format(question,*id)
        cursor.execute(qry)
        return HttpResponse("Ho gya bhyi")  