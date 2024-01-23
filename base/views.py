from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from base.models import Book
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email


        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(req):
    return Response('hello')


@api_view(['GET','POST','DELETE','PUT'])
def books(req,id=-1):
    if req.method =='GET':
        if id > -1:
             temp_book=Book.objects.get(id=id)
             return Response (BookSerializer(temp_book,many=False).data)
        all_books=BookSerializer(Book.objects.all(),many=True).data
        return Response (all_books)
    if req.method =='POST':
        book_serializer = BookSerializer(data=req.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response ("post done")
    if req.method =='DELETE':
        temp_book=Book.objects.get(id=id)
        temp_book.delete()
        return Response ("delete done")
    if req.method =='PUT':
        temp_book=Book.objects.get(id=id)
        ser = BookSerializer(data=req.data)
        old_book = Book.objects.get(id=id)
        res = ser.update(old_book, req.data)
        return Response("upd done")
