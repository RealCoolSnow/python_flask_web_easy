from flask_sqlalchemy import SQLAlchemy

from app.util.db_util import DBUtil
from app.util.redis_util import RedisUtil

dbutil = DBUtil()
redis = RedisUtil()
db = SQLAlchemy()
