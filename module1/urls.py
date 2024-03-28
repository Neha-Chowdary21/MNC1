from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = (
    path('hello/', hello1, name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpackage',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('randomcall/', randomcall, name='randomcall'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('getdate1/', getdate1, name='getdate1'),
    path('get_date/',get_date , name='get_date'),
    path('myregisterpage1/', myregisterpage1, name='myregisterpage1'),
    path('registerloginfunction/',registerloginfunction , name='registerloginfunction'),
    path('myfeedbackform1/', myfeedbackform1, name='myfeedbackform1'),
    path('feedbackformfunction/',feedbackformfunction , name='feedbackformfunction'),
    path('getPieChart/',getPieChart, name='getPieChart'),
    path('PieChart/',PieChart , name='PieChart'),
    path('Car',Car,name='Car'),
    path('weatherpagecall/',weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/',weatherlogic, name='weatherlogic'),
    path('login/',login, name='login'),
    path('login1/',login1, name='login1'),
    path('signup/',signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
)
