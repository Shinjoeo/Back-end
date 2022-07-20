from django.urls import path,include
from .views import NewWordViewSet,NewWordListCreateTime
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('newword',NewWordViewSet)

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
    path('list/', NewWordListCreateTime.as_view()),
#    path('listbylike/', NewWordList_LikeCount.as_view()),
    path('newword/', newword_list,name='newword'),
    path('newword/<int:pk>/', newword_one),
]