from .models import ReadingListItem
from rest_framework import viewsets
from .serializer import ReadingListItemSerializer

class ReadingListItemViewSet(viewsets.ModelViewSet):
    queryset = ReadingListItem.objects.all()
    serializer_class = ReadingListItemSerializer
