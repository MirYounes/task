from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()


class Rating(models.Model):
    user = models.ForeignKey(User, related_name="ratings", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="ratings", on_delete=models.CASCADE)
    rate = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.rate