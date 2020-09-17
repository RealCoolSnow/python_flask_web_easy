from flask import jsonify


class ResponseCode(object):
    SUCCESS = 0  # 成功
    FAIL = -1  # 失败


class RespBody(object):
    def __init__(self, data={}, code=ResponseCode.SUCCESS,
                 msg="success"):
        self._data = data
        self._msg = msg
        self._code = code

    def update(self, code=None, data=None, msg=None):
        if code is not None:
            self._code = code
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg

    def success(self, data=None, msg="success"):
        self.update(code=ResponseCode.SUCCESS, data=data, msg=msg)

    def fail(self, data=None, msg="fail"):
        self.update(code=ResponseCode.FAIL, data=data, msg=msg)

    @property
    def body(self):
        temp = self.__dict__
        temp["data"] = temp.pop("_data")
        temp["msg"] = temp.pop("_msg")
        temp["code"] = temp.pop("_code")
        return jsonify(temp)
