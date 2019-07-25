from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
        #related_name='+'는 related_name을 쓰지 않겠다는 뜻
        #related_name 중복을 피하려면 각각의 related_name을 지정해준다
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
