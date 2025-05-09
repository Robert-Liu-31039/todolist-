from django.contrib import admin

# . 代表的是在同一層的物件
from .models import Todo

# Register your models here.
admin.site.register(Todo)
