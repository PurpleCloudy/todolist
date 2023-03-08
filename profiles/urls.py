from django.urls import path
from profiles.views import ProfileView, MyLoginView, RegistrationView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name = 'login'),
    path('register/', RegistrationView.as_view(), name = 'register')
]