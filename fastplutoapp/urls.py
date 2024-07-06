from django.contrib import admin
from django.urls import path
from core import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    # inbuild urls to call admin dashboard
    path('admin/', admin.site.urls),
    path('', views.home),
    
    # authentication api's
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up', views.sign_up),
    
    
    # custom api's urls
    path('customer/', views.customer_page),
    path('courier/', views.courier_page)
]
