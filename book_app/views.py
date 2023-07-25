# from django.shortcuts import render

# Create your views here.

# 함수형 뷰
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(["GET"])
# def helloAPI(request):
#     return Response("hello world! 안녕")

# 클래스형 뷰
from rest_framework import viewsets, permissions, status, generics, mixins
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.filters import SearchFilter


# class HelloAPI(APIView):
#     def get(self, request, format=None):
#         return Response("hello world")


# class BooksAPI(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookAPI(APIView):
#     def get(self, request, bookno):
#         book = get_object_or_404(Book, bookno=bookno)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class BooksAPIMixins(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):  # GET 메소드 처리 함수 (전체 목록)
        return self.list(request, *args, **kwargs)  # mixins.ListModelMixin과 연결

    def post(self, request, *args, **kwargs):  # POST 메소드 처리 함수 (1권 등록)
        return self.create(request, *args, **kwargs)  # mixins.CreateModelMixin과 연결


class BookAPIMixins(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "bookno"  # 기본키

    # GET : bookno 전달 받고, bookno에 해당되는 1개의 도서 정보 반환 (retrieve)
    def get(self, request, *args, **kwargs):  # GET 메소드 처리 함수 (1권 조회)
        return self.retrieve(request, *args, **kwargs)  # mixins.RetrieveModelMixin와 연결

    # PUT : bookno 전달 받고, bookno에 해당되는 1개의 도서 정보 수정 (update)
    def put(self, request, *args, **kwargs):  # PUT 메소드 처리 함수 (1권 수정)
        return self.update(request, *args, **kwargs)  # mixins.UpdateModelMixin와 연결

    # DELETE : bookno 전달 받고, bookno에 해당되는 1개의 도서 정보 삭제 (destroy)
    def delete(self, request, *args, **kwargs):  # DELETE 메소드 처리 함수 (1권 삭제)
        return self.destroy(request, *args, **kwargs)  # mixins.DestroyModelMixin와 연결


# 도서 검색
class BookSearchList(generics.ListAPIView):
    serializer_class = BookSerializer
    lookup_field = "bookname"

    # 검색어 1개인 경우
    # def get_queryset(self):
    #     print(self.kwargs["keyword"])  # path variable : keyword
    #     #  path("search/<str:keyword>/", BookSearchList.as_view()),여기서 <str:keyword>이 path varialbe
    #     # return Book.objects.filter(bookname=self.kwargs["keyword"]) # 완전 일치하는 경우

    #     return Book.objects.filter(
    #         bookname__contains=self.kwargs["value"]
    #     )  # 포함 여부 (와일드 검색)

    # keyword, value 2개인 경우
    def get_queryset(self):
        print(self.kwargs["type"])  # path variable : keyword
        print(self.kwargs["keyword"])
        #  path("search/<str:keyword>/", BookSearchList.as_view()),여기서 <str:keyword>이 path varialbe
        # return Book.objects.filter(bookname=self.kwargs["keyword"]) # 완전 일치하는 경우

        if self.kwargs["type"] == "bookname":
            # lookup_field = "bookname"
            return Book.objects.filter(
                bookname__contains=self.kwargs["keyword"]
            )  # 포함 여부 (와일드 검색)
        else:
            lookup_field = "bookauthor"
            return Book.objects.filter(bookauthor__contains=self.kwargs["keyword"])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # 도서 테이블 차트 : 도서명/가격


class BooksChart(generics.ListAPIView):
    # queryset = Book.objects.all().order_by("-bookprice")
    serializer_class = BookSerializer
    lookup_field = "bookno"

    queryset = Book.objects.order_by("-bookprice").only("bookname", "bookprice")

    # def get_queryset(self):
    #     return Book.objects.only("bookname", "bookprice").order_by("-bookprice")

    def get(self, request, *args, **kwargs):  # GET 메소드 처리 함수 (전체 목록)
        return self.list(request, *args, **kwargs)
