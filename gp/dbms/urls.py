from django.urls import path
from . import views

urlpatterns = [
  path('', views.Login.as_view(), name ='dbms'),
  path('login/', views.Login.as_view(), name='login'),
  path('mainterface/', views.mainterface, name='mainterface'),
  path('logout/', views.logout, name='logout'),
  # path('regist/',views.regist, name='regist'),
  # path('index/',views.index,name = 'index'),
  # path('test/',views.test,name = 'test'),
]

