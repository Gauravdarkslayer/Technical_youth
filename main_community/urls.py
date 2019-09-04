from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('login1/',views.login1),
    path('signup/',views.signup),
    path('signup1/',views.Signnedup.as_view()),
    path('logout/',views.logout),
    
    path('getinterest/',views.getinterest),

    path('forgot/',views.render_forgot_template),
    path('forgots/',views.forgots),
    path('getotp/',views.getotp),
    path('updatePassword/',views.updatePassword),

    path('',include('question_posting.urls'))

]
