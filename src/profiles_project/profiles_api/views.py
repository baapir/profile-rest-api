# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models
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

        return Response({'message':'Hello', 'an_apiview':an_apiview})

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

class Helloviewsets(viewsets.ViewSet):
     """Test API ViewSet"""

     serializer_class = serializers.HelloSerializer

     def list(self, request):
         """Return a Hello Message"""

         a_viewset = [
             'uses actions (list, create, retrieve, update, partial_update)',
             'It is similar to triditional django view',
             'provides more fuctionality with less code',
             'Its mapped automaticly to URLs using Routers'
         ]
         return Response({'message':'Hello', 'a_viewset':a_viewset})

     def create(self, request):
         """Create a new hello message"""

         serializer = serializers.HelloSerializer(data = request.data)

         if serializer.is_valid():
             name = serializer.data.get('name')
             message = 'Hello {0}'.format(name)
             return Response({'message': message})
         else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def retrieve(self, request, pk=None):
         """Handles Getting an object by its id"""

         return Response({'http_method':'GET'})

     def update(Self, request, pk=None):
         """Handle updating an object"""

         return Response({'http_method':'PUT'})

     def partial_update(self, request, pk=None):
         """Handle upadating part of object"""

         return Response({'http_method':'PATCH'})

     def destroy(self, request, pk=None):
         """Handles removing an object"""

         return Response({'http_method':'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
