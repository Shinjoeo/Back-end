from django.urls import path
from .views import kakaoGetLogin, getUserInfo

urlpatterns = [
    path('accounts/kakao/login/', kakaoGetLogin),
    path('user/kakao/callback/', getUserInfo, name="kakao_callback"),
]