from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Todo, Category
from .forms import TodoForm, CategoryForm


@login_required
def todo_list(request):
    # فقط کارهای متعلق به کاربر فعلی
    todos = Todo.objects.filter(owner=request.user)

    # گرفتن مقادیر فیلترها از URL
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    category_id = request.GET.get('category')
    search = request.GET.get('search')

    # فیلتر وضعیت
    if status == 'completed':
        todos = todos.filter(completed=True)
    elif status == 'pending':
        todos = todos.filter(completed=False)

    # فیلتر اولویت
    if priority:
        todos = todos.filter(priority=priority)

    # فیلتر دسته‌بندی
    if category_id:
        todos = todos.filter(category_id=category_id)

    # جستجو
    if search:
        todos = todos.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    # دسته‌بندی‌های کاربر فعلی
    categories = Category.objects.filter(user=request.user)

    # آمار کلی بدون تأثیر گرفتن از فیلترها
    user_todos = Todo.objects.filter(owner=request.user)

    context = {
        'todos': todos,
        'categories': categories,

        # آمار
        'total_count': user_todos.count(),
        'completed_count': user_todos.filter(completed=True).count(),
        'pending_count': user_todos.filter(completed=False).count(),

        # فیلترهای انتخاب‌شده
        'selected_status': status,
        'selected_priority': priority,
        'selected_category': category_id,
        'search_query': search or '',
    }

    return render(request, 'todos/todo_list.html', context)


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, user=request.user)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.save()
            messages.success(
                request,
                f'کار "{todo.title}" با موفقیت اضافه شد!'
            )
            return redirect('todos:list')
    else:
        form = TodoForm(user=request.user)
    
    return render(
        request,
        'todos/todo_form.html',
        {'form': form, 'action': 'ایجاد'}
    )


@login_required
def todo_update(request, pk):
    todo = get_object_or_404(
        Todo,
        pk=pk,
        owner=request.user
    )
    
    if request.method == 'POST':
        form = TodoForm(
            request.POST,
            instance=todo,
            user=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'کار "{todo.title}" با موفقیت بروزرسانی شد!'
            )
            return redirect('todos:list')
    else:
        form = TodoForm(
            instance=todo,
            user=request.user
        )
    
    return render(
        request,
        'todos/todo_form.html',
        {
            'form': form,
            'action': 'ویرایش',
            'todo': todo
        }
    )


@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(
        Todo,
        pk=pk,
        owner=request.user
    )
    
    if request.method == 'POST':
        title = todo.title
        todo.delete()
        messages.success(
            request,
            f'کار "{title}" با موفقیت حذف شد!'
        )
        return redirect('todos:list')
    
    return render(
        request,
        'todos/todo_confirm_delete.html',
        {'todo': todo}
    )


@login_required
def todo_toggle(request, pk):
    todo = get_object_or_404(
        Todo,
        pk=pk,
        owner=request.user
    )
    
    todo.completed = not todo.completed
    todo.save()
    
    status = (
        'تکمیل شد'
        if todo.completed
        else 'به حالت در انتظار برگشت'
    )
    
    messages.success(
        request,
        f'کار "{todo.title}" {status}!'
    )
    
    return redirect('todos:list')


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(
                request,
                f'دسته‌بندی "{category.name}" اضافه شد!'
            )
            return redirect('todos:create')
    else:
        form = CategoryForm()
    
    return render(
        request,
        'todos/category_form.html',
        {'form': form}
    )