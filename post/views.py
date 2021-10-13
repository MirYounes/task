from rest_framework import generics, permissions
from django.conf import settings
from django.core.cache import cache
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer
from .models import Post


class PostPagination(PageNumberPagination):
    page_size = settings.PAGINATION_POST
    page_size_query_param = 'page_size'
    max_page_size = settings.PAGINATION_MAX_POST  


class PostListApi(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = None
        if 'posts' in cache:
            queryset = cache.get('posts')
        else :
            queryset = Post.objects.all()
            cache.set('posts', queryset, settings.CACHE_TIMEOUT_POSTS)
        
        return queryset
