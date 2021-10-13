from django.urls import path, include


app_name = 'api'
urlpatterns = [
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('posts/', include('post.urls', namespace='post'))    
]
