from django.urls import path
from .views import Register, Login, Validate_token

urlpatterns = [
    path('register',Register.as_view()),
    path('login',Login.as_view()),
    path('validatetoken',Validate_token.as_view())
]