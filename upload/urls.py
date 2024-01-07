from django.contrib import admin
from django.urls import path
from upload.views import ImageView, PostViewSet

urlpatterns = [
    path('post/',PostViewSet.as_view({'post': 'create'})),
    path('images/<int:pk>/', ImageView.as_view())
]