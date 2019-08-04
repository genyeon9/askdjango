from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . models import Post
from django.core.urlresolvers import reverse_lazy

post_list = ListView.as_view(model=Post, paginate_by=10)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
#reverse는 초기화되는 시점과 동시에 가동되므로 모든 장고 프로젝트가 초기화 되고 난 후 사용가능
#reverse_lazy는 초기화 되고 난 후로 가동 시점을 지연시켜줌