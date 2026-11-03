from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import ProfileRetreiveView
from accounts.views import SignUpView

urlpatterns = [

    path('register/',SignUpView.as_view()),
    
    path('login/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),

    path('profile/',ProfileRetreiveView.as_view()),
]