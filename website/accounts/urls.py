from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
        path('', views.index_view, name='index_view'),
        path('logout_view/', views.logout_view, name='logout_view'),
        path('login_view/', views.login_view, name='login_view' ),
        path('loginme/', views.loginme, name='loginme'),
        path('register_view/', views.register_view, name='register_view'),
        path('accounts/',include('allauth.urls')),
]
