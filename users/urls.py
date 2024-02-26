from django.urls import path
from .views import HomeView, SignUpView, SignInView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),
]
