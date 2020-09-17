from app.libs import dbutil


class UserService:
    db = dbutil

    def __init__(self):
        pass

    def total(self):
        count = self.db.count("wx_user")
        return str(count)
