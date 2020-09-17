import redis


class RedisUtil(object):
    conn = redis.StrictRedis(host="127.0.0.1", port=6379)

    @classmethod
    def get(cls, key):
        """获取key所对应的值"""
        return cls.conn.get(key)

    @classmethod
    def set(cls, key, value, expire=3600):
        """设置值"""
        return cls.conn.set(key, value, ex=expire)

    @classmethod
    def delete(cls, key):
        """删除值"""
        result = cls.conn.keys()
        if bytes(key, encoding="utf-8") in result:
            return cls.conn.delete(key)
        else:
            return "此%s不存在" % key


if __name__ == '__main__':
    pass
