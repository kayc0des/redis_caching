"""
There's no goal. Just messing around with Redis.
"""

import redis
from config import Settings

if __name__ == '__main__':
    redis_sess = redis.Redis(host=Settings.REDIS_HOST, port=Settings.REDIS_PORT, db=Settings.REDIS_DB, decode_responses=True)
    
    redis_sess.set('username', 'kayc0des', ex=20)
    print(redis_sess.get('username'))
    