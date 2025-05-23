from django.shortcuts import render, redirect

from .models import Todo

from .forms import TodoForm

from datetime import datetime


# Create your views here.
def todolist(request):  # Django 規定 : 一定要帶 request 這個參數
    user = request.user

    todos = None

    ## .get() -> 回傳唯一物件，但並非容器型別
    # todos = [Todo.objects.get(id=1)]

    ## .filter() -> 回傳符合篩選的資料，容器型別
    # todos = Todo.objects.filter(id=1)

    ## .all() -> 取得所有的資料，容器型別
    # todos = Todo.objects.all()

    # 如果有登入帳號的話，僅顯示登入者的 todo 內容
    if user.is_authenticated:
        filter_params = request.GET.get("filter")

        print(filter_params)

        # .order_by("-@欄位名稱") -> 代表降冪排序
        # .order_by("@欄位名稱") -> 代表升冪排序
        todos = Todo.objects.filter(user=request.user).order_by("-created")
        # todos = Todo.objects.filter(user=request.user).order_by("created")

        if filter_params == "important":
            todos = todos.filter(important=True).order_by("-created")
        elif filter_params == "pending":
            todos = todos.filter(completed=False).order_by("-created")
        elif filter_params == "completed":
            todos = todos.filter(completed=True).order_by("-created")

    result = {"todos": todos, "user": user}

    return render(request, "todo/todolist.html", result)


def viewtodo(request, id):  # Django 規定 : 一定要帶 request 這個參數
    todo = None
    form = None
    message = None

    try:
        todo = Todo.objects.get(id=id)

        if request.method == "GET":
            # instance -> 實際案例，代表要放在 TodoForm 的資料實例
            form = TodoForm(instance=todo)
        else:
            # 將 原本 form 的內容記憶起來，並取代 原本instance 的資料，用於執行 Update
            form = TodoForm(request.POST, instance=todo)

            # 暫存，不做 commit，因為還有資料要做處理
            action = form.save(commit=False)
            if action.completed == True:
                action.date_completed = datetime.now()
            else:
                action.date_completed = None

            # 真的存於 db 中
            action.save()

            message = "修改成功"

    except Exception as e:
        print(e)

    return render(
        request, "todo/viewtodo.html", {"todo": todo, "form": form, "message": message}
    )


def createtodo(request):  # Django 規定 : 一定要帶 request 這個參數
    if request.method == "POST":
        # 將 原本 form 的內容記憶起來，用於執行 Insert
        form = TodoForm(request.POST)

        # 暫存，不做 commit，因為還有資料要做處理
        todo = form.save(commit=False)
        todo.user = request.user

        if todo.completed == True:
            todo.date_completed = datetime.now()
        else:
            todo.date_completed = None

        # 真的存於 db 中
        todo.save()

        return redirect("todolist")
    else:
        form = TodoForm

    return render(request, "todo/createtodo.html", {"form": form})


def deletetodo(request, id):  # Django 規定 : 一定要帶 request 這個參數
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect("todolist")
