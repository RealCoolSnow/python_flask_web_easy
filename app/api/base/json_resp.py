from flask import Response, jsonify


class JsonResp(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        print(response)
        if isinstance(response, dict):
            response = jsonify(response)
        return super().force_type(response, environ)
