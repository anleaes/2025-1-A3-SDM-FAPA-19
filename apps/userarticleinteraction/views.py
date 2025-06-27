from .models import UserArticleInteraction
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import UserArticleInteractionSerializer

class UserArticleInteractionViewSet(viewsets.ModelViewSet):
    queryset = UserArticleInteraction.objects.all()
    serializer_class = UserArticleInteractionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return UserArticleInteraction.objects.filter(user=self.request.user)
