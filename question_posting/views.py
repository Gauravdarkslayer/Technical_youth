from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import pymysql as sql
# Create your views here.

def all_posts(request):
    #with connection.cursor() as cursor:
    db = sql.connect(host='localhost',port=3306,database='techinal_youth',user="root",password='')
    cursor = db.cursor()
    cursor.execute("select post from posts")
    blogs=cursor.fetchall()
    b=[]
    for var in blogs:
        dict={
            'post':"".join(var)
        }
        b.append(dict['post'])
        # print(b)
    db.commit()
    return render(request,"allblog.html",{'all':b})

def question_post(request):
   return render(request,'question_post.html')

def postnewquestion(request):
    question=request.POST.get("question_field")
    email=request.COOKIES['emailid']
    #with connection.cursor() as cusrsor:
    db = sql.connect(host='localhost',port=3306,database='techinal_youth',user="root",password='')
    cursor = db.cursor()
    qry2=f"select id from user where emailid='{email}'"
    cursor.execute(qry2)
    id=int(cursor.fetchone()[0])
    # print(id)
    # print(email)
    qry=f"insert into posts (post,userid) values ('{question}','{id}')" #BUG HERE IN SPECIAL CHARACTERS
    cursor.execute(qry)
    db.commit()
    # return HttpResponse("<h1 style='color:blue'>question posted successfully</h1>")
    return render(request,"colorlib-regform-7/dialoganswer.html")

def post_answer(request):
    return render(request,"dialogbox.html")
