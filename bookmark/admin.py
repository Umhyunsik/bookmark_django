from django.contrib import admin

# Register your models here.
# 내가만든 모델을 관리자페이지에서 관리할수있도록 등록
from .models import Bookmark
admin.site.register(Bookmark)