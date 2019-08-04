from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login_form.html',
                                     authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout'),
    path('profile/', views.profile, name='profile'),

]
