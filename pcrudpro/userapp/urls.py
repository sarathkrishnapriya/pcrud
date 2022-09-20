from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('registration', views.registraion_home,name='ride_user_reg'),
    path('',views.riderLoginView,name='rider_login') ,
    path('home',views.HomepageView,name='rider_home'),
    path('logout',views.logout,name='rider_logout'), 
    path('profile',views.ProfileView,name='rider_profile'),
    path('update',views.UpdateView,name='rider_update'),
    path('updateuser',views.UpdateUserView,name='rider_user_update'),
    path('riderhome',views.backProfileView,name='backhome')
]