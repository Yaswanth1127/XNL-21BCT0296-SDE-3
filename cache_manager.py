import redis
import json

class CacheManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def set_cache(self, key, value, expiry=3600):
        self.client.set(key, json.dumps(value), ex=expiry)

    def get_cache(self, key):
        data = self.client.get(key)
        if data:
            return json.loads(data)
        return None

    def delete_cache(self, key):
        self.client.delete(key)

