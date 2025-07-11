#pages/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_client, name='login'),
    path('signup/', views.signup, name='signup'),    
    path('confirm/', views.confirm_email, name='confirm_email'),

    path('reset_password1/', views.reset_password1, name='reset_password1'),
    path('reset_password2/', views.reset_password2, name='reset_password2'),
    path('reset_password3/', views.reset_password3, name='reset_password3'),
    path('reset_password4/', views.reset_password4, name='reset_password4'),

    path('home_user/', views.home_user, name='home_user'),
    path('logout/', views.logout_view, name='logout'), 
    path('logout_admin/', views.logout_admin, name='logout_admin'), 
    path('home_user/add_service/', views.add_service, name='add_service'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
    
    # admin
    path('admin_login/', views.admin_login, name='admin_login'),
    path('home_admin/', views.home_admin, name='home_admin'),

    path('check_request/<int:service_id>/', views.check_request, name='check_request'),
    path('reject_request/<int:service_id>/', views.reject_request, name='reject_request'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)