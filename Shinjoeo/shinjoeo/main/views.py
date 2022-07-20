from django.shortcuts import render
from .models import NewWord
from .serializers import NewWordSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

#글 작성, 수정
class NewWordViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer


#최신순정렬(default)
#검색 url예제
#http://127.0.0.1:8000/main/list/?searchword=%EC%A0%9C%EB%AA%A91
class NewWordList_CreateTime(ListAPIView):
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer
    
    def get_queryset(self):
        queryset = NewWord.objects.all()
        searchword = self.request.query_params.get('searchword')
        if searchword is not None:
            queryset = queryset.filter(word__contains=searchword)
        return queryset

#좋아요순
# class NewWordList_LikeCount(ListAPIView):
#     queryset = NewWord.objects.all().order_by('')
#     serializer_class = NewWordSerializer

#검색