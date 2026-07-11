from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class MeView(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,request):
        user = request.user
        
        return Response({
            'id':user.id,
            'username':user.username,
            'email': user.email,
            'phone_number': 'user.phone_number',
        })