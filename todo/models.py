from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)

    # 在字串型別中，blank=True 代表可以為空字串
    text = models.TextField(blank=True)

    # 時間型別中，auto_now_add=True 代表自動帶入現在的時間
    created = models.DateTimeField(auto_now_add=True)

    # 時間型別中，null=True 代表時間型別為空物件
    data_completed = models.DateTimeField(null=True, blank=True)

    # ※ 字串會用空字串 -> blank=True
    # ※ 物件會用空物件 -> null=True

    important = models.BooleanField(default=False)

    # __str__ 是 models.Model 內的既有函式，
    # 功能只是在 Django 的 管理後端，
    # 將 該資料庫的 資料的顯示 名稱做自定義的顯示
    def __str__(self):  # self 代表是要取同個 model 內的物件
        # id 是 table 預設一定會有的欄位
        return f"{self.id} - {self.title} - {self.created}"
