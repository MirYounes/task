from django.conf import settings
import redis


redis = redis.Redis(host='127.0.0.1', port='6379', db=2)


def add_to_redis(post_id,rate):
    post_name = f'{settings.REDIS_POST_PREFIX}_{post_id}'

    if redis.exists(post_name):
        redis.hincrby(post_name, 'total_rate', rate)
        redis.hincrby(post_name, 'numbers_rate', 1)
    else :
        redis.hset(post_name, 'total_rate', rate)
        redis.hset(post_name, 'numbers_rate', 1)


def get_from_redis(post_id):
    post_name = f'{settings.REDIS_PREFIX_POST}_{post_id}'

    if redis.exists(post_name):
        data = {key.decode('utf-8'): value.decode('utf-8')
                for key, value in redis.hgetall(post_name).items()}
    else :
        data = {
            'total_rate':0,
            'numbers_rate':0
        }
    
    return data