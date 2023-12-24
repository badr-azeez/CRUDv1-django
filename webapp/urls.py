from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.my_login,name='login'),
    path('logout',views.my_logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create-record',views.CreateRecord,name='create-record'),
    path('update-record/<int:pk>',views.UpdateRecord,name='update-record'),
    path('view-record/<int:pk>',views.SingleRecord,name='view-record')
]
