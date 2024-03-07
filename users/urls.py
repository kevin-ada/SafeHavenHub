from django.urls import path
from .views import HomeView, signup_view, sign_in_view, logout_view, ContactUsView, AboutUsView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('signup/', signup_view, name='signup'),
    path('signin/', sign_in_view, name='sign_in'),
    path('logout/', logout_view, name='logout'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('about-us/', AboutUsView.as_view(), name='about'),
]
