import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse

# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.') #길이 제한 있는 문자열
    content = models.TextField(verbose_name='내용') #길이 제한 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='경도/위도 포맷으로 입력',
        validators=[lnglat_validator],
        )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True) #같은 app내에 있는 클래스를 지정할때 클래스가 뒤에서 지정되어도 ''으로 지정가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id'] #'-'붙이면 내림차순 정렬(최근 것부터 보여줌)

    def __str__(self):   #title이 제목값으로 보여지도록 처리함
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #Post가 삭제되면 연결된 다수의 post를 모두 삭제해주겠다.
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):    #Tag set에서 name이 보여지도록 하기 위함
        return self.name