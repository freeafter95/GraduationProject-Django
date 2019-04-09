from django.urls import path
from . import views
urlpatterns = [
  path('',views.login, name ='login'),
  path('login/',views.login, name='login'),
  # path('regist/',views.regist, name='regist'),
  # path('index/',views.index,name = 'index'),
  # path('logout/',views.logout,name = 'logout'),
  # path('test/',views.test,name = 'test'),
]

