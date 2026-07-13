from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('todos:list')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(
            self.request,
            f'خوش آمدید {user.username}! ثبت‌نام شما با موفقیت انجام شد.'
        )
        return redirect(self.success_url)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('todos:list')
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request,
                f'خوش آمدید {user.get_full_name()}!'
            )
            next_url = request.GET.get('next', 'todos:list')
            return redirect(next_url)
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(
        request,
        'شما با موفقیت از سیستم خارج شدید.'
    )
    return redirect('accounts:login')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'پروفایل شما با موفقیت بروزرسانی شد.'
            )
            return redirect('accounts:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {
        'form': form,
        'total_todos': request.user.todos.count(),
        'completed_todos': request.user.todos.filter(completed=True).count(),
        'pending_todos': request.user.todos.filter(completed=False).count(),
    }
    
    return render(request, 'accounts/profile.html', context)