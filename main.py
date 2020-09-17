import os
import platform
import time

from flask import Flask
from flask_cors import *

from app.api.base.resp_body import RespBody
from app.api.user import user
from config import config

app = Flask(__name__)
test = (os.name == 'nt')
app.config.from_object(config['development' if test else 'production'])
CORS(app, supports_credentials=app.config['DEBUG'])
# app.response_class = JsonResp
app.register_blueprint(user)

print(app.config)


@app.route('/')
def index():
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    resp = RespBody()
    resp.success(data={"time": str_time, "python_ver": platform.python_version()})
    return resp.body


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
