from django.shortcuts import HttpResponse , redirect
from django.core import serializers

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

def base(request):
    if request.method == "POST":
        return HttpResponse('post')
    else:
        py_data = {
            "success" : 1,
            "name": "subhadip",
            "age" : 28
        }

        json_data = JSONRenderer().render(py_data)
        return HttpResponse(json_data , content_type="application/json")





# @api_view(['GET', 'POST'])
def test(request):
    if request.method == "POST":
        try:
            py_data = JSONParser().parse(request)
        except :
            return Response({'error':1},status=status.HTTP_400_BAD_REQUEST)
        
        py_data["success"] = 1
        return Response(py_data)
    else:
        py_data = {
            "success" : 1,
            "name": "subhadip",
            "age" : 28
        }
        return Response(py_data)
       
   



      