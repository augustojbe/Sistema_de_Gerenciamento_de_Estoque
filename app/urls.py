from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_login
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_login.LoginView.as_view(), name='login'),
    path('logout/', auth_login.LogoutView.as_view(), name='logout'),

    path('api/v1/', include('authentication.urls')),

    path('', views.home, name='home'),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
]
