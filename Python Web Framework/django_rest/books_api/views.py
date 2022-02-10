from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books_api.models import BookModel
from books_api.serializers import BookSerializer


class BookListCreate(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):
    def put(self, request, book_pk):
        book = get_object_or_404(BookModel, pk=book_pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request, book_pk):
        try:
            current_book = BookModel.objects.get(pk=book_pk)
            book_serializer = BookSerializer(current_book)
            return Response(book_serializer.data)
        except:
            return Response({'message': 'da ama ne'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, book_pk):
        try:
            book = BookModel.objects.get(pk=book_pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'msg': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
