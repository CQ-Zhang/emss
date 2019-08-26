from django.urls import path
from emsapp import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register,name= 'register'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),
    path('registerlogic/', views.registerlogic, name='registerlogic'),
    path('home/', views.home, name='home'),
]