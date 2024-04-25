from django.urls import path
from .import views

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
]
