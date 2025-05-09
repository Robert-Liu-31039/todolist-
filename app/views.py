from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


# Create your views here.
def hello(request):  # Django 規定 : 一定要帶 request 這個參數
    result = {"message": "測試", "data": 123, "label": "文字"}

    # Django 的規範 :
    # 要傳回的結果不可以單純為字串，
    # return "123" <- 會錯誤
    # 必須要經過包裝為 HttpResponse or JsonResponse
    # return HttpResponse("<h1>Hello!</h1>")
    return JsonResponse(result)


def lotto(request):  # Django 規定 : 一定要帶 request 這個參數
    # 1~49 不重複 6 個數字跟排序
    numbers = sorted(random.sample(range(1, 50), 6))
    numbers = ",".join((str(i) for i in numbers))
    # numbers = ",".join(map(str,numbers))

    spec_number = random.randint(1, 49)

    result = {"numbers": numbers, "spec_number": spec_number}

    # return JsonResponse(result)

    # 渲染 template 的格式在 Django 也有規定 :
    # 第一個參數一定要是 request,
    # 第二個參數是 template,
    # 第三個參數是 data
    return render(request, "lotto.html", result)
