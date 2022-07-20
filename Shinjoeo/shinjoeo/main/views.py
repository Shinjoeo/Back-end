from django.shortcuts import render
from .models import NewWord
from .serializers import NewWordSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

# Create your views here.
class NewWordViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer

class NewWordListAPI(ListAPIView):
    queryset = NewWord.objects.all()
    serializer_class = NewWordSerializer