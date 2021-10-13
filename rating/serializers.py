from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from post.models import Post
from .models import Rating
from .utils import add_to_redis


class ReatingSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    rate = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])

    def create(self, validated_data):
        user =  self.context['request'].user

        # get the post
        try :
            post = Post.objects.get(id=validated_data['post_id'])
        except Post.DoesNotExist :
            raise serializers.ValidationError("post with thid id does not exist")
        
        # create rate object
        rate = Rating.objects.create(user=user, post=post, rate=validated_data['rate'])

        # add rate to redis
        add_to_redis(post.id, rate.rate)

        return rate
    
    def update(self, instance, validated_data):
        old_rate = instance.rate

        instance.rate = validated_data['rate']
        instance.save()

        add_to_redis(validated_data['post_id'], instance.rate-old_rate)

        return instance