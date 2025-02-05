from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignupForm, LoginForm


class SignupView(CreateView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Регистрация успешно завершена!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка при регистрации. Пожалуйста, проверьте введенные данные!")
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request=self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            remember_me = form.cleaned_data.get('remember_me', False)
            if not remember_me:
                self.request.session.set_expiry(0)
            messages.success(self.request, "Вы успешно вошли в систему!")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Неверный email или пароль. Попробуйте снова!")
            return self.form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы успешно вышли из системы!")
        return super().dispatch(request, *args, **kwargs)


def profile_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Для доступа к профилю необходимо войти в систему!")
        return redirect('users:login')
    return render(request, 'users/signup.html')


