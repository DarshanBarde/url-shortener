from django.urls import path
from .views import RegisterView,ShortenURLView,DashboardView,redirect_to_original,generate_qr_code
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('shorten/', ShortenURLView.as_view(), name='shorten_url'), 
    path('qr/<str:short_code>/', generate_qr_code, name='generate_qr_code'),
    path('<str:short_code>/', redirect_to_original, name='redirect_to_original'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]