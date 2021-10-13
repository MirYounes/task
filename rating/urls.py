from django.urls import path
from .views import AddRateSerializer


app_name = 'rating'
urlpatterns = [
    path('add/<int:post_id>/', AddRateSerializer.as_view(), name='add_rate')
]
