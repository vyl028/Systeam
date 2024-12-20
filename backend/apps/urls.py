from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.apps.views import UserViewSet, ActivityViewSet, ArticleViewSet, PostViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 