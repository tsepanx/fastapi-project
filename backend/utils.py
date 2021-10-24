import redis
import uuid


def generate_hash(length=5):
    return uuid.uuid4().hex[:length]


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class RedisManager(metaclass=SingletonMeta):
    def __init__(self, host="localhost", port=6379, pwd=""):
        self.__r = redis.StrictRedis(host=host, port=port, password=pwd, decode_responses=True)

    def get_item(self, key: str):
        return self.__r.get(key)

    def set_item(self, key, value):
        return self.__r.set(key, value)

    def set_dict(self, key: str, d: dict):
        return self.__r.hmset(key, d)

    def get_dict(self, key: str):
        return self.__r.hgetall(key)

    def delete(self, key: str):
        return self.__r.delete(key)

    def list_keys(self, pattern="*"):
        return self.__r.keys(pattern)

    def exists(self, item_id: str):
        return self.__r.exists(item_id)
