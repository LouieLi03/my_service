from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
from VideoLib.models import User


def test(request):
    return JsonResponse(data={
        "status": 200,
        "msg": "",
    })


def register(request):
    if request.method == "POST":
        username = request.GET.get("username"),
        mobile_no = request.GET.get("username"),
        avatar = request.GET.get("username"),
        sex = request.GET.get("username"),
        if username and mobile_no:
            user = User()
            user.username = username;
            user.mobile_no = mobile_no;
    return None