from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import backends as backend
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer
import qrcode
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import get_object_or_404, redirect

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)


class ShortenURLView(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)




def generate_qr_code(request, short_code):
    url = ShortenedURL.objects.get(short_code=short_code).original_url
    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer)
    buffer.seek(0)
    return HttpResponse(buffer, content_type="image/png")



def redirect_to_original(request, short_code):
    short_url = get_object_or_404(ShortenedURL, short_code=short_code)
    short_url.visit_count += 1
    short_url.save()
    return redirect(short_url.original_url)


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        urls = ShortenedURL.objects.filter(user=request.user)
        data = [{"original_url": u.original_url, "short_code": u.short_code, "visit_count": u.visit_count} for u in urls]
        return Response(data)

