from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MarloUserSerializer, MarloProductListSerializer
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from .models import MarloUser, MarloProduct
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_product': '/product',
        'Limit_Product': '/product/?limit=4',
        'Csv file upload from admin panel through only superuser can do it': '/admin',
        'login': '/login',
        'register': '/register',
    }
 
    return Response(api_urls)

class MarloProductListView(ListAPIView):
  queryset = MarloProduct.objects.all()
  serializer_class = MarloProductListSerializer
  pagination_class = LimitOffsetPagination



# Create your views here.
@api_view(['POST'])
def Marlo_registerUser(request):
    if request.method == 'POST':
        serializer = MarloUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Marlo_user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = MarloUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Marlo_user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
