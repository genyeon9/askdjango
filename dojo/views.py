from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import os
from django.conf import settings
from .forms import PostForm
from .models import Post

# Create your views here.

def post_new(request):
    if request.method == 'POST':
        #POST인자는 request.POST와 request.FILES를 제공받음
        form = PostForm(request.POST, request.FILES) #순서 바뀌면 안 됨
        if form.is_valid():  #유효성 검사 통과 못하면 오류정보와 같이 form값에 보낸다
            #방법1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()
            #방법2)
            '''
            post = Post(title=form.cleaned_data['title'],
            content=form.cleaned_data['content'])
            post.save()
            '''
            #방법3)
            '''
            post = Post.objects.create(title=form.cleaned_data['title'],
            content=form.cleaned_data['content'])
            '''
            #방법4)
            #post = Post.objects.create(**form.cleaned_data)

            #방법5)
            post = form.save(commit=False) #어차피 밑에서 post.save()할 것이므로 임의로 commit값을  정해서 save의 여부를 정할 수 있다
            post.ip = request.META('REMOTE_ADDR')
            post.save()
            return redirect('dojo:post_new') #namespace:name 쓸 것을 권장
    else:
        form = PostForm()
    return render(request,'dojo/post_form.html', {'form':form})


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META.get('REMOTE_ADDR')
            post.save()
            return redirect('dojo:post_new')
    else:
        form = PostForm(instance=post)
    return render(request,'dojo/post_form.html', {'form':form})



def mysum(request, numbers):
    result = sum(map(lambda x:int(x or 0),numbers.split('/')))
    return HttpResponse(result)



def hello(request,name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))



def post_list1(request):
    name = 'jinhyeon'
    return  HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))



def post_list2(request):
    name = 'jinhyeon'
    return render(request, 'dojo/post_list2.html', {'name':name})



def post_list3(request):
    return JsonResponse({
        'message': '안녕, 파이썬&장고',
        'items':['파이썬', '장고', 'Celery', 'Azure', 'AWS']
    }, json_dumps_params={'ensure_ascii': False})



def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'test.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response