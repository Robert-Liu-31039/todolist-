from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def user_register(request):
    message = ""
    if request.method == "POST":
        # 印出 request.POST 的結果
        print("POST!", request.POST)

        # 將 原本 form 的內容記憶起來
        form = UserCreationForm(request.POST)

        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(username, password1, password2)

        if password1 != password2:
            message = "兩次密碼不相同!"
        elif len(password1) < 8:
            message = "密碼過短!"
        else:
            # 使用 Django 內建的函數 驗證 使用者是否存在
            user = User.objects.filter(username=username)
            if user:
                message = "使用者已存在!"
            else:
                # 使用 Django 內建的函數 建立 使用者資料
                userInfo = User.objects.create_user(
                    username=username, password=password1
                )
                userInfo.save()
                message = "註冊成功!"

                return redirect("login")
    else:
        # UserCreationForm() 是 Django 內建的函數 用於產生 註冊使用者 的前端 html 資料
        form = UserCreationForm()

    return render(request, "user/register.html", {"form": form, "message": message})


def user_login(request):
    message = ""
    username = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)

        user = authenticate(request, username=username, password=password)

        if not user:
            message = "帳號或密碼錯誤!"
        else:
            login(request, user)
            message = "登入成功!"

            # 網頁跳轉至 path name="todolist" 的頁面
            return redirect("todolist")

    return render(
        request, "user/login.html", {"username": username, "message": message}
    )


def user_logout(request):
    logout(request)
    return redirect("todolist")
