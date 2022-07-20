from django.shortcuts import get_object_or_404
from .models import NewWord
from .serializers import NewWordSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#글 작성, 수정
class NewWordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer

    # def post_like(self,request,pk):
    #      queryset = NewWord.objects.all()
    #      newword = get_object_or_404(queryset, id=pk)
    #      user = request.user
    #      user = User.objects.get(user=user)
    #      check_liker = user.likeword.filter(id=pk)
    #      if check_liker.exists():
    #          user.check_liker.remove(newword)
    #          # newword.like_count -= 1
    #          newword.save()
    #      else:
    #          user.check_liker.add(newword)
    #          # post.like_count += 1
    #          newword.save()
    #      return Response({'newword_id':'Successfully activated'},status=status.HTTP_200_OK)


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
