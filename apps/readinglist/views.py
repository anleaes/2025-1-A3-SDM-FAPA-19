from .models import ReadingList
from rest_framework import viewsets
from .serializer import ReadingListSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ReadingListViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return ReadingList.objects.filter(user=self.request.user)
    serializer_class = ReadingListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        