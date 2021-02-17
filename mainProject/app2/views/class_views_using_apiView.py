from rest_framework.views import APIView
from rest_framework.response import Response

from app2.models import ArtifactModel
from app2.serializers import ArtifactSerializers

class Class_APiView (APIView):
    def get(self, request) :
        artifacts = ArtifactModel.objects.all()
        arti_serializer = ArtifactSerializers(artifacts ,many=True)

        return Response({
            'success': True,
            'data':arti_serializer.data
        })

    def post(self , request , *args ,**kwargs):
        if request.data.get('name') != '':
            arti_serializer = ArtifactSerializers(data=request.data)
            if arti_serializer.is_valid():
                arti_serializer.save()
            return Response({
                'success': True,
                'data':arti_serializer.data
            })