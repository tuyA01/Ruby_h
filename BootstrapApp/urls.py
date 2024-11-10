from django.urls import path
from BootstrapApp import views




urlpatterns=[
    path('',views.home,name='my_home')

]