from django.urls import path, include
from rest_framework import routers

from projects.views import ProjectApiView
from tasks.views import TaskOperationViewSet

app_name = 'projects'

router = routers.DefaultRouter()
router.register('', ProjectApiView, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:project_id>/tasks/', TaskOperationViewSet.as_view(), name='task-operation'),
]
