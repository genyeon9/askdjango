from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from . models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '') #q가 있으면 가져오고 없으면 빈 문자열
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html',{
        'post_list':qs
    })

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, id=id)  #지정 Record가 없는 것은 서버오류(500)가 아니므로 404오류로 바꿔줘야 한다.

    return render(request, 'blog/post_detail.html', {
        'post':post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) #PostForm에서 모델을 Post로 지정해주었기 때문에 form은 PostForm의 인스턴스이자 Post의 인스턴스?
        if form.is_valid():
            post = form.save()
            return redirect(post) #Post 모델에 get_absolute_url 함수를 정의했으므로 인스턴스를 넣어주기만 해도 url을 추적할 수 있다
    else:                         #따라서 post_detail에 쉽게 접근 가능
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) #PostForm에서 모델을 Post로 지정해주었기 때문에 form은 PostForm의 인스턴스이자 Post의 인스턴스?
        if form.is_valid():
            post = form.save()
            return redirect(post) #Post 모델에 get_absolute_url 함수를 정의했으므로 인스턴스를 넣어주기만 해도 url을 추적할 수 있다
    else:                         #따라서 post_detail에 쉽게 접근 가능
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })