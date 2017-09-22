# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
# Create your views here.
class Helloapiview(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
             'uses http method as functions()',
             'It is similar to triditional django view',
             'Gives you must control on your logic',
             'Its mapped manully to URLs'
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle ubdating object"""

        return Response({'method' : 'put'})

    def patch(self, request, pk=None):
        """Patch request only updates fields provided in the request"""

        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object"""

        return Response({'method' : 'delete'})
