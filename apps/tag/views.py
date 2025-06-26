from .models import Tag
from rest_framework import viewsets
from .serializer import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
