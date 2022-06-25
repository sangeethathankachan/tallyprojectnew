from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('changecompony',views.changecompony,name='changecompony'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('creategroup',views.creategroup,name='creategroup'),
    path('crtcompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony')

]