from django.urls import path
from. import views


urlpatterns = [

    path('', views.demo, name='demo'),
    path('login', views.login1, name='login1'),
    path('register', views.newUser, name='newUser'),
    path('button', views.button, name='button'),
    path('form', views.form, name='form'),
    path('index', views.index, name='index'),
    path('github',views.github,name='github'),



]
