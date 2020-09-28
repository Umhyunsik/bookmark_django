from django.shortcuts import render

# Create your views here.
# CRUD : CREATE Read Update Delete
# LIST

# 클래스형 뷰(기본적으로 만들어져있는거) , 함수형 뷰(이것저것 하고싶은거)
#웹페이지에 접속한다. -> 페이지를 본다
# url 입력 -> 웹서버가 뷰를 찾아서 동작 시킨다 -> 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from .models import Bookmark
class BookmarkListView(ListView):
    model=Bookmark


class BookmarkCreatView(CreateView):
    model=Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'
    success_url =reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model=Bookmark
class BookmarkUpdateView(UpdateView):
    model=Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'
class BookmarkDeleteView(DeleteView):
    model=Bookmark
    #라우팅 테이블이 다불러지지않은 상태에서 클래스뷰가 먼저 점검해서 오류발생할수있어서 리버스레이지 무조건 써야한다
    success_url = reverse_lazy('list')


