from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import RegisterAPIView, LoginAPIView, UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),
]
