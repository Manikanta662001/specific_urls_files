from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('a1_first/',a1_first,name='a1_first'),
    path('a1_second/',a1_second,name='a1_second')
]