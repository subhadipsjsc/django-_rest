
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app2.models import ArtifactModel
from app2.serializers import ArtifactSerializers

@api_view(['GET','POST'])
def func_blog_view(request):
    if request.method == 'GET' :
        artifacts = ArtifactModel.objects.all()
        arti_serializer = ArtifactSerializers(artifacts ,many=True)

        return Response({
            'success': True,
            'data':arti_serializer.data
        })
    if request.method == 'POST':
        return Response({
            'success': True,
            'data':"POST method data"
        })

    return Response({
        'success': False,
        'data':"Only GET and POST supported"
    })