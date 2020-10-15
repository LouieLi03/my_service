import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse
# Create your views here.
from Tools.http_helper import REQUEST_SUCCESS, REQUEST_FAILURE
from VideoLib.models import User


def test(request):
    return JsonResponse(data={
        "status": 200,
        "msg": "",
    })


def register(request):
    data = {
        "status": REQUEST_FAILURE,
        "msg": "请求错误"
    }

    if request.method == "POST":
        username_tuple = request.POST.get("username"),
        mobile_no_tuple = request.POST.get("mobileNo"),
        avatar_tuple = request.POST.get("avatar"),
        sex_tuple = request.POST.get("sex"),
        password_tuple = request.POST.get("password"),

        user = User()
        if mobile_no_tuple[0]:
            user.mobile_no = mobile_no_tuple[0]
        else:
            data["msg"] = "请填写手机号"

        if username_tuple[0]:
            user.username = username_tuple[0]
        else:
            user.username = mobile_no_tuple[0]

        if password_tuple[0]:
            # django自带算法
            password = make_password(password_tuple[0])
            user.password = password
        else:
            data["msg"] = "请填写密码"

        if avatar_tuple[0]:
            user.avatar = avatar_tuple[0]

        if sex_tuple[0]:
            sex = sex_tuple[0]
            if sex != 0 and sex != 1 and sex != 2:
                data["msg"] = "请选择正确的性别信息"
            user.sex = sex

        if len(data["msg"]) <= 0 or data["msg"] == "请求错误":
            check_user = User.objects.filter(mobile_no=user.mobile_no)
            if check_user.exists():
                data["msg"] = "手机号已注册，请直接登录"
            else:
                try:
                    data["status"] = REQUEST_SUCCESS
                    data["msg"] = "注册成功"
                    user.save()
                except Exception as e:
                    print(e)
                    data["msg"] = e

    return JsonResponse(data=data)


def login(request):
    data = {
        "status": REQUEST_FAILURE,
        "msg": "账号或密码不正确，请重新输入"
    }

    if request.method == "POST":
        mobile_no_tuple = request.POST.get("mobileNo"),
        password_tuple = request.POST.get("password"),
        mobile_no = mobile_no_tuple[0]
        password = password_tuple[0]
        user = User.objects.filter(mobile_no=mobile_no)
        if user.exists():
            user = user.first()
            # 校验密码
            if check_password(password, user.password):
                # 生成token
                token = uuid.uuid4().hex.upper()
                # 写入缓存 redis
                cache.set(token, mobile_no, timeout=60 * 60 * 24 * 7)
                user.token = token
                user.save()
                data["msg"] = "登录成功！"
                data["status"] = REQUEST_SUCCESS
                data["data"] = user.toDict()

    return JsonResponse(data=data)


def updateUserInfo(request):
    data = {
        "status": REQUEST_FAILURE,
        "msg": "参数有问题"
    }
    if request.method == "POST":
        mobile_no_tuple = request.POST.get("mobileNo"),
        token_tuple = request.POST.get("token"),
        mobile_no = mobile_no_tuple[0]
        token = token_tuple[0]

        c_mobile_no = cache.get(token)

        if c_mobile_no == mobile_no:
            user = User.objects.filter(mobile_no=mobile_no)
            if user.exists():
                user = user.first()

                avatar_tuple = request.POST.get("avatar"),
                if len(avatar_tuple):
                    avatar = avatar_tuple[0]
                    user.avatar = avatar

                username_tuple = request.POST.get("username"),
                if len(username_tuple):
                    username = username_tuple[0]
                    user.username = username

                mobile_no_tuple = request.POST.get("mobile_no"),
                if len(mobile_no_tuple):
                    mobile_no = mobile_no_tuple[0]
                    user.mobile_no = mobile_no

                user.save()
                data["msg"] = "修改信息成功！"
                data["status"] = REQUEST_SUCCESS
                data["data"] = user.toDict()

    return JsonResponse(data=data)