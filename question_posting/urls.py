from django.urls import path
from . import views
urlpatterns = [
     path('posts/',views.all_posts),
     path('question_post/',views.question_post),
     path('post_it/',views.postnewquestion),
     path('all_posts/',views.all_posts)
]