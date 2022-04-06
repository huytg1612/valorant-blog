from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import UserModel
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken

from ValorantReddit import settings
from reddit.domain import UserDomain
from reddit.models import User
from reddit.serializers import UserSerializer, UserLoginSerializer


# Code API
# class UserRegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
#             serializer.save()
#
#             return JsonResponse({
#                 'message': 'Register successful!'
#             }, status=status.HTTP_201_CREATED)
#
#         else:
#             return JsonResponse({
#                 'error_message': 'This email has already exist!',
#                 'errors_code': 400,
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserLoginView(APIView):
#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = authenticate(
#                 request,
#                 username=serializer.validated_data['email'],
#                 password=serializer.validated_data['password']
#             )
#             if user:
#                 refresh = TokenObtainPairSerializer.get_token(user)
#                 data = {
#                     'refresh_token': str(refresh),
#                     'access_token': str(refresh.access_token),
#                 }
#                 return Response(data, status=status.HTTP_200_OK)
#
#             return Response({
#                 'error_message': 'Email or password is incorrect!',
#                 'error_code': 400
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response({
#             'error_messages': serializer.errors,
#             'error_code': 400
#         }, status=status.HTTP_400_BAD_REQUEST)
#
# class UserDetailView(APIView):
#     def get(self, request, token):
#         userDomain = UserDomain()
#         user = userDomain.getUserFromToken(token)
#         if user:
#             data = {
#                 'email': user.email,
#                 'password': user.password
#             }
#             return Response(data, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 'error_message': 'HTTP_401_UNAUTHORIZED',
#                 'error_code': 401
#             }, status=status.HTTP_401_UNAUTHORIZED)
def login_user(request):
    if request.method == 'POST':
        data = {
            'email': request.POST['email'],
            'password': request.POST['password'],
        }
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                login(request, user)
                return redirect('blog:index')
            else:
                data_res = {
                    "code": 400,
                    "message": "Email or password is incorrect!"
                }
                return render(request, 'pages/login.html', data_res)
        data_res = {
            "code": 400,
            "message": serializer.errors
        }
        return render(request, 'pages/login.html', data_res)
    else:

        return render(request, 'pages/login.html')


def register(request):
    if request.method == 'POST':
        data = {
            'email': request.POST['email'],
            'password': request.POST['password'],
        }
        serializer = UserSerializer(data=data)
        if data['password'] == request.POST['re_password']:
            if serializer.is_valid():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()

                return render(request, 'pages/login.html')

            else:
                data_res = {
                    "code": 400,
                    "message": "User is exist"
                }
                return render(request, 'pages/register.html', data_res)
        else:
            print('Pwd')
            data_res = {
                "code": 400,
                "message": "Password not match"
            }
            return render(request, 'pages/register.html', data_res)
    else:
        return render(request, 'pages/register.html')
