from django.shortcuts import get_object_or_404
from uritemplate import partial
from .models import NewWord
from .serializers import NewWordSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404
import sys


#글 작성, 수정
class NewWordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer

    def update(self, request, pk):
        queryset = NewWord.objects.all()
        newword_id = pk
        newword = get_object_or_404(queryset, id=pk)
        user = request.user
        user_ob = User.objects.get(username=user)
        newword.like_user_ids.add(user_ob)
        print(user_ob.username)
        # return redirect("http://localhost:8000/main/list/")
       # return Response(status=status.HTTP_200_OK)
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
# class NewWordList_LikeCount(ListAPIView):
#     queryset = NewWord.objects.all().order_by('')
#     serializer_class = NewWordSerializer
