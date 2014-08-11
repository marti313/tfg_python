from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import BookSerializer, KeywordSerializer, SubjectSerializer
from models import Book, Keyword, Subject
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

class BookListAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        permission_classes=(AllowAny,)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDetailAPI(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk) #atajo de django
        permission_classes=(AllowAny,)
        serializer = BookSerializer(book)
        return Response(serializer.data)




class KeywordListAPI(APIView):
    def get(self, request):
        keyword = Keyword.objects.all()
        permission_classes=(AllowAny,)
        serializer = KeywordSerializer(keyword, many=True)
        return Response(serializer.data)

class KeywordDetailAPI(APIView):

    def get(self, request, pk):
        keyword = get_object_or_404(Keyword, pk=pk) #atajo de django
        serializer = KeywordSerializer(keyword)
        return Response(serializer.data)


class SubjectListAPI(APIView):
    def get(self, request):
        subject = Subject.objects.all()
        permission_classes=(AllowAny,)
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

class SubjectDetailAPI(APIView):

    def get(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk) #atajo de django
        permission_classes=(AllowAny,)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)


