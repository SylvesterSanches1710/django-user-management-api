from django.shortcuts import get_object_or_404, render
from users.models import UserProfile
from users.serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_list(request):
  if request.method == 'GET':
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)
    
  if request.method == 'POST':
    serializer = UserProfileSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request,pk):
  user = get_object_or_404(UserProfile, pk=pk)

  if request.method == 'GET':
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

  if request.method == 'PUT':
      serializer = UserProfileSerializer(user,data=request.data)

      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)  
      
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'DELETE':
      user.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)