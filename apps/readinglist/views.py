from .models import ReadingList
from rest_framework import viewsets
from .serializer import ReadingListSerializer

class ReadingListViewSet(viewsets.ModelViewSet):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
