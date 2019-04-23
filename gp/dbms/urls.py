from django.urls import path
from . import views

urlpatterns = [
  path('', views.Login.as_view(), name ='dbms'),
  path('login/', views.Login.as_view(), name='login'),
  path('mainterface/', views.mainterface, name='mainterface'),
  path('logout/', views.logout, name='logout'),
  path('crystalselect/', views.crystal_select, name='crystal_select'),
  path('crystalinsert/', views.crystal_insert, name='crystal_insert'),
  path('processselect/', views.process_select, name='process_select'),
  path('processinsert/', views.process_insert, name='process_insert'),
  path('testselect/', views.test_select, name='test_select'),
  path('testinsert/', views.test_insert, name='test_insert'),
  path('maingraph/', views.main_graph, name='maingraph'),
  # path('regist/',views.regist, name='regist'),
  # path('index/',views.index,name = 'index'),
  # path('test/',views.test,name = 'test'),
]

