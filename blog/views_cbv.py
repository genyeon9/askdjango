from django.views.generic import CreateView, ListView
from . models import Post
from django import forms

post_list = ListView.as_view(model=Post, paginate_by=10)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

post_new = PostCreateView.as_view()