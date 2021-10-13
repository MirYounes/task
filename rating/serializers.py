from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingSerializer(serializers.Serializer):
    rate = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])