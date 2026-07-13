from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Todo, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'color', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('name', 'user__username')
    ordering = ('name',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'priority', 'completed', 'category', 'due_date', 'created_at')
    list_filter = ('completed', 'priority', 'category', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('اطلاعات اصلی', {'fields': ('owner', 'title', 'description')}),
        ('تنظیمات', {'fields': ('priority', 'category', 'completed', 'due_date')}),
    )