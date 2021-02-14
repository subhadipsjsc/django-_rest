from rest_framework import viewsets

from .models import Artifact
from .serializers import ArtifactSerializers

# Create your views here.

class ArtifactViewSets(viewsets.ModelViewSet) :
    serializer_class = ArtifactSerializers
    def get_queryset(self):
        return Artifact.objects.all()
