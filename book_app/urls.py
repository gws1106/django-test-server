from django.urls import path, include

# from .views import BookAPI, BooksAPI
from .views import BooksAPIMixins, BookAPIMixins, BookSearchList, BooksChart

# from .views import helloAPI

urlpatterns = [
    # path("hello/", helloAPI),
    # path("books/", BooksAPI.as_view()),
    # path("book/<str:bookno>/", BookAPI.as_view()),
    path("books/", BooksAPIMixins.as_view()),
    path("book/<str:bookno>/", BookAPIMixins.as_view()),
    path("search/<str:type>/<str:keyword>/", BookSearchList.as_view()),
    path("search/<str:keyword>/", BookSearchList.as_view()),
    path("chart_db/", BooksChart.as_view()),
    # chart_file 추가할 것
]
