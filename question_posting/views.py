from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
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
