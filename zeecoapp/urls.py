from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.index , name="index"),
    path('pwered/', views.botts , name="predict")
]