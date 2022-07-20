from django.contrib import admin
from django.urls import path, include
from accounts.views import getUserInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/callback/', getUserInfo),
]
