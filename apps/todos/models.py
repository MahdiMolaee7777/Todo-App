from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField('نام', max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='کاربر'
    )
    color = models.CharField('رنگ', max_length=7, default='#007bff')
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        unique_together = ['name', 'user']
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'زیاد'),
    ]
    
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos',
        verbose_name='صاحب'
    )
    title = models.CharField('عنوان', max_length=200)
    description = models.TextField('توضیحات', blank=True)
    completed = models.BooleanField('تکمیل شده', default=False)
    priority = models.CharField(
        'اولویت',
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='todos',
        verbose_name='دسته‌بندی'
    )
    due_date = models.DateField('مهلت انجام', null=True, blank=True)
    
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField('آخرین بروزرسانی', auto_now=True)
    
    class Meta:
        verbose_name = 'کار'
        verbose_name_plural = 'کارها'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        from django.utils import timezone
        
        if self.due_date and not self.completed:
            return timezone.now() > self.due_date
        return False