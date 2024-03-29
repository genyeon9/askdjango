from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Create your models here.

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    user_agent = models.CharField(max_length=200, blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                   choices=(
                                       ('A', 'A서버'),
                                       ('B', 'B서버'),
                                       ('C', 'C서버'),
                                   ))
    user_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])

    class Meta:
        unique_together = [
            ('server_name', 'user_name'),
        ]
    def __str__(self):
        return self.user_name





