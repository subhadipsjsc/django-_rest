from rest_framework import serializers
from .models import ArtifactModel

class ArtifactSerializers(serializers.ModelSerializer):
    class Meta:
        model= ArtifactModel
        fields = "__all__"