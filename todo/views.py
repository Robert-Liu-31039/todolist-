from django.shortcuts import render

from .models import Todo


# Create your views here.
def todolist(request):

    # .all() -> 取得所有的資料，容器型別
    todos = Todo.objects.all()

    # .get() -> 回傳唯一物件，但並非容器型別
    todos = [Todo.objects.get(id=1)]

    # .filter() -> 回傳符合篩選的資料，容器型別
    todos = Todo.objects.filter(id=1)

    result = {"todos": todos}

    return render(request, "todo/todolist.html", result)
