# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class Helloapiview(APIView):
    """Test API view"""


    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
             'uses http method as functions()',
             'It is similar to triditional django view',
             'Gives you must control on your logic',
             'Its mapped manully to URLs'
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})
