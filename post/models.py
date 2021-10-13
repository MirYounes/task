from django.db import models
from rating.utils import get_from_redis


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    @property
    def numbers_rate(self):
        result = get_from_redis(self.id)
        return result['numbers_rate']

    @property
    def avg_rate(self):
        result = get_from_redis(self.id)
        try :
            return result['total_rate']/result['numbers_rate']
        except :
            return 0