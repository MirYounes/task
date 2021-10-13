from re import S
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from post.models import Post
from .serializers import RatingSerializer
from .models import Rating
from .utils import add_rate_to_redis , update_rate_to_redis


class AddRateSerializer(generics.GenericAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request, post_id):
        serializer = self.serializer_class(data=request.data , context = {'request':request,})
        serializer.is_valid(raise_exception=True)

        # get the post
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return serializers.ValidationError('post does not exist')

        # get the rate object
        try:
            rate = Rating.objects.get(user=request.user, post=post)
            old_rate = rate.rate
            
            rate.rate = serializer.validated_data['rate']
            rate.save()

            update_rate_to_redis(post.id, rate.rate-old_rate)
            content = {"message":"rate updated"}

        except Rating.DoesNotExist:
            rate = Rating.objects.create(user=request.user, 
                    post=post, rate=serializer.validated_data['rate'])
            add_rate_to_redis(post.id, rate.rate)
            content = {"message":"rate added"}
        
        return Response(content, status=status.HTTP_200_OK)