from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
@api_view(['POST'])
def registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # refresh = RefreshToken.for_user(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.filter(username=username).first()
    if user is None:
        return Response({'error': 'Invalid Credentials'})
    if not user.check_password(password):
        return Response({'error': 'Invalid Credentials'})
    refresh = RefreshToken.for_user(user)
    return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
# Create your views here.
class Createbookview(generics.CreateAPIView):
    serializer_class=bokserializer
    def perform_create(self,serializer):
        user_id=self.kwargs['user_id']
        user=User.objects.get(id=user_id)
        serializer.save(user=user)
class bookview(generics.ListAPIView):
    serializer_class=bokserializer
    def get_queryset(self):
        user_id=self.kwargs['user_id']
        return bookcreate.objects.filter(user_id=user_id)
class postbook(generics.CreateAPIView):
    queryset=book.objects.all()
    serializer_class=bookserializers
class listbook(generics.ListAPIView):
    queryset=book.objects.all()
    serializer_class=bookserializers
class upostbook(generics.CreateAPIView):
    queryset=book.objects.all()
    serializer_class=ubookserializers
class issuepostbook(generics.CreateAPIView):
    queryset=book.objects.all()
    serializer_class=issuebookserializers
class returnpostbook(generics.CreateAPIView):
    queryset=book.objects.all()
    serializer_class=returnbookserializers