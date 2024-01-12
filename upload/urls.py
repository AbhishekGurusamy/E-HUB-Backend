from django.contrib import admin
from django.urls import path
from upload.views import ImageView, LoginImageView

urlpatterns = [
    path('post',LoginImageView.as_view()),
    path('images/<int:pk>/', ImageView.as_view())
]