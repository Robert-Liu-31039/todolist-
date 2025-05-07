from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def hello(request):
    result = {"message": "測試", "data": 123, "label": "文字"}

    # Django 的規範 :
    # 要傳回的結果不可以單純為字串，
    # 必須要經過包裝為 HttpResponse or JsonResponse
    # return HttpResponse("<h1>Hello!</h1>")
    return JsonResponse(result)
