from rest_framework.routers import SimpleRouter
from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
