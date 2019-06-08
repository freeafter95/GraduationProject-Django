from django.urls import path
from . import views

urlpatterns = [
  path('', views.Login.as_view(), name ='dbms'),
  path('login/', views.Login.as_view(), name='login'),
  path('mainterface/', views.mainterface, name='mainterface'),
  path('logout/', views.logout, name='logout'),
  path('literatureselect/', views.literature_select, name='literature_select'),
  path('literatureinsert/', views.literature_insert, name='literature_insert'),
  path('literaturequery/', views.literature_query, name='literature_query'),
  path('literaturedelete-<int:id>/', views.literature_delete, name='literature_delete'),
  path('literatureupdate-<int:id>/', views.literature_update, name='literature_update'),
  path('literatureallin/', views.literature_allin, name='literature_allin'),
  path('literatureallout/', views.literature_allout, name='literature_allout'),
  path('crystalselect/', views.crystal_select, name='crystal_select'),
  path('crystalinsert/', views.crystal_insert, name='crystal_insert'),
  path('crystalquery/', views.crystal_query, name='crystal_query'),
  path('crystaldelete-<int:id>/', views.crystal_delete, name='crystal_delete'),
  path('crystalupdate-<int:id>/', views.crystal_update, name='crystal_update'),
  path('crystalallin/', views.crystal_allin, name='crystal_allin'),
  path('crystalallout/', views.crystal_allout, name='crystal_allout'),
  path('processselect/', views.process_select, name='process_select'),
  path('processinsert/', views.process_insert, name='process_insert'),
  path('processquery/', views.process_query, name='process_query'),
  path('processdelete-<int:id>/', views.process_delete, name='process_delete'),
  path('processupdate-<int:id>/', views.process_update, name='process_update'),
  path('processallin/', views.process_allin, name='process_allin'),
  path('processallout/', views.process_allout, name='process_allout'),
  path('testselect/', views.test_select, name='test_select'),
  path('testinsert/', views.test_insert, name='test_insert'),
  path('testquery/', views.test_query, name='test_query'),
  path('testdelete-<int:id>/', views.test_delete, name='test_delete'),
  path('testupdate-<int:id>/', views.test_update, name='test_update'),
  path('testallin/', views.test_allin, name='test_allin'),
  path('testallout/', views.test_allout, name='test_allout'),
  path('radiationselect/', views.radiation_select, name='radiation_select'),
  path('radiationinsert/', views.radiation_insert, name='radiation_insert'),
  path('radiationquery/', views.radiation_query, name='radiation_query'),
  path('radiationdelete-<int:id>/', views.radiation_delete, name='radiation_delete'),
  path('radiationupdate-<int:id>/', views.radiation_update, name='radiation_update'),
  path('radiationallin/', views.radiation_allin, name='radiation_allin'),
  path('radiationallout/', views.radiation_allout, name='radiation_allout'),
  path('pictureselect/', views.picture_select, name='picture_select'),
  path('picturequery/', views.picture_query, name='picture_query'),
  path('picturedelete-<int:id>/', views.picture_delete, name='picture_delete'),
  path('maingraph/', views.main_graph, name='maingraph'),
  path('usermanage/', views.user_manage, name='usermanage'),
  path('adduser/', views.add_user, name='adduser'),
  path('first<int:p1>-<int:p2>/', views.first, name='first'),
  path('compute/', views.compute, name='compute'),
  path('deluser-<str:username>/', views.del_user, name='deluser'),
  # path('regist/',views.regist, name='regist'),
  # path('index/',views.index,name = 'index'),
  # path('test/',views.test,name = 'test'),
]

