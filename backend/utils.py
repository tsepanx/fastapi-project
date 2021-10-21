import redis
import random, string

import logging


def list_wrapper(func):
    def wrapper(*args, **kwargs):
        return ''.join(func(*args, **kwargs))

    return wrapper


@list_wrapper
def gen_id(length=5):
    chars = string.ascii_lowercase + string.digits * 2
    for i in range(length):
        yield random.choice(chars)


class RedisManager:
    ITEM_PREFIX = "id_"

    @classmethod
    def build_key(cls, item_id, prefix=ITEM_PREFIX):
        return prefix + item_id

    def __init__(self, host="localhost", port=6379, pwd=""):
        self.__r = redis.StrictRedis(host=host, port=port, password=pwd, decode_responses=True)

    def __get(self, key: str):
        return self.__r.get(key)

    def __set(self, key, value):
        return self.__r.set(key, value)

    def __mset(self, d: dict):
        return self.__r.mset(d)

    def __mget(self, keys):
        return self.__r.mget(keys)

    def __clear(self):
        return self.__r.flushall()

    def get_item(self, item_id: str, prefix=ITEM_PREFIX):
        key = RedisManager.build_key(item_id, prefix)
        return self.__get(key)

    def set_item(self, item_id: str, value, prefix=ITEM_PREFIX):
        key = RedisManager.build_key(item_id, prefix)
        return self.__set(key, value)

    def list_keys(self, pattern="*"):
        return self.__r.keys(pattern)

    def exists_item(self, item_id: str, prefix=ITEM_PREFIX):
        key = RedisManager.build_key(item_id, prefix)
        return self.__r.exists(key)
