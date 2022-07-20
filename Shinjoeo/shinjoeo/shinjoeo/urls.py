from django.contrib import admin
from django.urls import path, include
from accounts.views import getUserInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('accounts/kakao/login/callback/', getUserInfo),
]
