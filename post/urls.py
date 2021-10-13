from django.urls import path
from .views import PostListApi


app_name = "post"
urlpatterns = [
    path('',PostListApi.as_view(), name='pot_list'),
]
