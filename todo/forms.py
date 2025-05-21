from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        # 宣告 form 使用的是哪個 model
        model = Todo

        # fields 代表要使用的欄位有哪些
        ## "__all__" 代表 table 所有的欄位都要
        ##fields = "__all__"

        # 指定 要的欄位有哪些
        fields = ["title", "text", "important", "completed"]
