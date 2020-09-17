from flask import Blueprint

from app.api.base.resp_body import RespBody
from app.service.user_service import UserService

user = Blueprint('user', __name__, url_prefix='/user')
userService = UserService()


@user.route('/')
def index():
    return 'this is user model'


@user.route('/count')
def user_count():
    resp = RespBody()
    resp.success(data={"total": userService.total()})
    return resp.body
