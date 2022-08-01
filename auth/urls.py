from django.urls import path
from auth.views import (
    MyObtainTokenPairView, 
    RegisterView, 
    LoginView, 
    UpdateProfileView, 
    HelloView
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', HelloView.as_view(), name='home'),
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
]