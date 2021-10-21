import redis
import random, string

import logging


def list_wrapper(func):
    def wrapper(*args, **kwargs):
        return ''.join(func(*args, **kwargs))

    return wrapper


@list_wrapper
def generate_hash(length=5):
    chars = string.ascii_lowercase + string.digits * 2
    for i in range(length):
        yield random.choice(chars)


class RedisManager:
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

    def exists_item(self, item_id: str):
        return self.__r.exists(item_id)
