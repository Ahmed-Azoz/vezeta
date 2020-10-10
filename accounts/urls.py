
from django.urls import path
from . import views

app_name= 'accounts'

urlpatterns = [
    path('doctors/', views.doctors_List, name='doctors_List'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('update_profile/', views.update_profile, name='updateprofile'),
    path('<slug:slug>/', views.doctors_details, name='doctors_detail'),

]



