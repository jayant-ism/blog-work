from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home") ,
    path('campgrounds-index', views.campgroundsindex, name="campgroundsindex") ,
    path('campgroundopen', views.campgroundopen, name="campgroundopen") ,
    path('campgroundaddcom', views.campgroundaddcom , name="campgroundaddcom") ,
    path('login', views.login, name="login"),
    path('register', views.register, name="register") ,
    path('control', views.controllog, name="controllog") ,
    path('comallo', views.comallo, name="comallo") ,
    path('comrem', views.comrem, name="comrem") ,
    
    path('add', views.add, name="add") ,
    path('submit', views.submit, name="submit") ,
    path('userdetails', views.userdetails, name="userdetails") ,
    path('logout', views.logouts, name="logouts") ,
    path('changepass', views.changepass, name="changepass") ,
    path('descadd', views.descadd, name="descadd") ,
    path('imgchange', views.imgchange , name="imgchange") ,
    path('iconchange', views.iconchange , name="iconchange") ,
    
    path('search', views.search , name="search") ,
    
    path('deletepost', views.deletepost , name="deletepost") ,
    
    
 

]
