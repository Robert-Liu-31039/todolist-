from django.shortcuts import render

from .models import Todo


# Create your views here.
def todolist(request):  # Django 規定 : 一定要帶 request 這個參數
    user = request.user

    # .get() -> 回傳唯一物件，但並非容器型別
    todos = [Todo.objects.get(id=1)]

    # .filter() -> 回傳符合篩選的資料，容器型別
    todos = Todo.objects.filter(id=1)

    # .all() -> 取得所有的資料，容器型別
    todos = Todo.objects.all()

    result = {"todos": todos, "user": user}

    return render(request, "todo/todolist.html", result)


def viewtodo(request, id):  # Django 規定 : 一定要帶 request 這個參數
    todo = None

    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/viewtodo.html", {"todo": todo})
