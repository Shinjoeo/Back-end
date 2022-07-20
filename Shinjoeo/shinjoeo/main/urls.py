from django.urls import path,include
from .views import NewWordViewSet,NewWordListAPI
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register('newword',NewWordViewSet,basename ='newword')

#신조어 목록 보여주기 + 새로운 게시글 생성
newword_list = NewWordViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

#신조어 삭제, 좋아요
newword_one = NewWordViewSet.as_view({
    # 'get': 'retrieve',
    'delete': 'destroy',
    'post_like': 'create',
})

urlpatterns =[
    path('', include(router.urls)),
    path('list/', NewWordListAPI.as_view()),
    path('newword/', newword_list),
    path('newword/<int:pk>/', newword_one),
]