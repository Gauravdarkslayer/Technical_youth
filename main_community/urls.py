from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    # path('home/',views.home),
    path('login/',views.login),
    path('signup/',views.signup)
]
