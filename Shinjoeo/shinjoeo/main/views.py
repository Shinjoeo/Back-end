from django.shortcuts import get_object_or_404
from django.db.models import Count
from .models import NewWord
from .serializers import NewWordSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User




#글 작성, 수정
class NewWordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer

    def update(self, request, pk):
        queryset = NewWord.objects.all()
        newword = get_object_or_404(queryset, id=pk)
        user = request.user
        user_ob = User.objects.get(username=user)
        newword.like_user_ids.add(user_ob)
        return Response({"active":"Success"},status=status.HTTP_200_OK)
        

#최신순정렬(default)
#검색 url예제
#http://127.0.0.1:8000/main/list/?searchword=%EC%A0%9C%EB%AA%A91

class NewWordListCreateTime(ListAPIView):
    serializer_class = NewWordSerializer
    
    def get_queryset(self):
        queryset = NewWord.objects.all().order_by('-create_time')
        searchword = self.request.query_params.get('searchword')
        if searchword is not None:
            queryset = queryset.filter(word__contains=searchword)
        return queryset

#좋아요순
class NewWordListLikeCount(ListAPIView):
    serializer_class = NewWordSerializer

    def get_queryset(self):
        queryset = NewWord.objects.annotate(q_count=Count('like_user_ids')).order_by('-q_count')
        return queryset
