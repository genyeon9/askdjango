from .models import Post
from django import forms

''' #ModelForm으로 만들었다면 validator함수는 model.py에서 정의하고 사용
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')
'''

'''
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
'''

class PostForm(forms.ModelForm): #ModelForm은 위와 같은 save함수의 기능을 자동 수행함
    class Meta:
        model = Post
        #fields = '__all__' #모델의 모든 필드값을 Form의 필드값으로 지정
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }