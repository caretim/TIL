from django.contrib import admin
from django.urls import path,include
from . import views



# 앱의 이름을 지정하여 변수로 사용가능
app_name= "testapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path("detail/<int:pk>",views.detail,name='detail'),
    path("delete/<int:pk>",views.delete,name='delete'),
    path("update/<int:pk>",views.update,name='update'),
]