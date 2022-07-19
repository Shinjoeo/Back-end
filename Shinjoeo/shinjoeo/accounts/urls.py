from django.urls import path
from .views import kakaoGetLogin, getUserInfo, kakaoGetLogout

urlpatterns = [
    path('login/', kakaoGetLogin),
    path('user/kakao/callback/', getUserInfo, name="kakao_callback"),
    path('logout/', kakaoGetLogout),
]