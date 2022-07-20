from django.shortcuts import render
from .models import NewWord
from .serializers import NewWordSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics, status

# Create your views here.
class NewWordViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self,request):
        queryset = NewWord.objects.all()
        serializer_class = NewWordSerializer
    def post_like(self,request,newword_id):
        queryset = NewWord.objects.all()
        newword = get_object_or_404(NewWord, id=newword_id)
        user = request.user
        user = User.objects.get(user=user)

        check_liker = user.likeword.filter(id=newword_id)

        if check_liker.exists():
            user.check_liker.remove(newword)
            # newword.like_count -= 1
            newword.save()
        else:
            user.check_liker.add(newword)
            # post.like_count += 1
            newword.save()

        return Response({'newword_id':'Successfully activated'},status=status.HTTP_200_OK)

class NewWordListAPI(ListAPIView):
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer

