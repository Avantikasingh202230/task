from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('register/', registration),
    path('login/', login),
    path('postbook/',postbook.as_view()),
    path('listbook',listbook.as_view()),
    path('userbook/',upostbook.as_view()),
    path('issuebook/',issuepostbook.as_view()),
    path('returnbook/',returnpostbook.as_view()),
    path('bookrecord/<int:user_id>/',Createbookview.as_view()),
    path('list/<int:user_id>/',bookview.as_view())
]