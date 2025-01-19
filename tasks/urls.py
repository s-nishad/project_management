from django.urls import path, include
from rest_framework import routers

from tasks.views import TaskViewSet, CommentViewSet, CommentListCreateView

app_name = 'tasks'

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='tasks')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('task/<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-operation'),
]
