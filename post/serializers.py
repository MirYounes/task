from rest_framework import serializers
from rating.models import Rating
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    numbers_rate = serializers.ReadOnlyField()
    avg_rate = serializers.ReadOnlyField()
    user_rate = serializers.SerializerMethodField('get_user_rate')

    class Meta:
        model = Post
        fields = ['title','body','numbers_rate','avg_rate','user_rate']
    
    def get_user_rate(self, obj):
        user =  self.context['request'].user
        
        try :
            rate = Rating.objects.get(user=user,post=obj)
        except Rating.DoesNotExist:
            return None

        return rate.rate