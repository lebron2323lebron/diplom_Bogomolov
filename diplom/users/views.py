from django.views.generic import DetailView, UpdateView, CreateView
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from users.forms import LoginForm


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    next_page = 'home'


class UserLogoutView(LogoutView):
    """
    Выход с сайта
    """
    next_page = 'index'




class UserProfileView(TemplateView):  

    def __init__(self, **kwargs: reverse_lazy) -> None:
        super().__init__(**kwargs)
        self.template_name = 'users/profile_detail.html'  

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        try:  
            user = get_object_or_404(User, username=self.kwargs.get('username'))  
        except User.DoesNotExist:  
            raise Http404("Пользователь не найден")  
        context['user_profile'] = user
        if user.groups.all().__len__()<1:
            context['user_group'] = 'Пользователь'
        else:
            context['user_group'] = user.groups.all()[0]
        if 'Механик' in context['user_group'].__str__():
            self.template_name = 'users/profile_detail_mechanik.html' 
        elif 'Управляющий' in context['user_group'].__str__(): 
            self.template_name = 'users/profile_detail_mechanik2.html' 
        context['title'] = f'Профиль пользователя {user}'  
        return context


class ProfileUpdateView(UpdateView):
    """
    Представление для редактирования профиля
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'slug': self.object.slug})


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_success_url(self):  
        return reverse_lazy('users:login')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


def get_my_courses(request):
    return render(request, "users/profile-courses.html", context={"courses": request.user.courses.all()})


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'base/edit_profile_page.html'
    form_class=UserProfileView
    
    success_url = reverse_lazy('profile')