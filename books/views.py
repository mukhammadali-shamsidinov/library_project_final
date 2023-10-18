from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import Book
from .models import Books


# class BookListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Book

class BookListApiView(APIView):

    def get(self,request):
        books = Books.objects.all()
        serializer = Book(books,many=True).data

        data = {
            "status":"success",
            "book":serializer

        }

        return Response(data)


# class BookListApiDetailView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = Book

class BookListApiDetailView(APIView):
    def get(self,request,pk):
        try:
            data = Books.objects.get(id=pk)
            serializer = Book(data).data

            return Response(
                {"status":status.HTTP_200_OK,
                 "data":serializer
                 }
            )
        except Exception:
            return Response(
                {
                    "status":False,
                    "message":"Eror"
                }
            )


class BookDeleteApi(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = Book
class BookUpdateApi(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = Book
# @api_view(['GET'])
# def book_list_view(request,*args,**kwargs):
#     book = Books.objects.all()
#     serializer = Book(book,many=True)
#     return Response(serializer.data)

# class CreateListApiView(generics.CreateAPIView):
#     queryset = Books
#     serializer_class = Book


class CreateListApiView(APIView):

    def post(self,request):
        data = request.data
        serializer = Book(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message":"Success",
                    "status":status.HTTP_201_CREATED
                }
            )
        else:
            Response(
                {"message":"error",
                 "status":status.HTTP_400_BAD_REQUEST
                 }
            )


class BookingListViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = Book
