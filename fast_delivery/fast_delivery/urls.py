from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('sign-in/', auth_views.LoginView.as_view(template_name='signin.html')),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/')),

    path('customer/', views.customer_page),
    path('courier/', views.couriew_page),
]
