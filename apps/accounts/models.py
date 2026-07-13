from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('ایمیل', unique=True)
    username = models.CharField('نام کاربری', max_length=150, unique=True)
    first_name = models.CharField('نام', max_length=150, blank=True)
    last_name = models.CharField('نام خانوادگی', max_length=150, blank=True)
    avatar = models.ImageField(
        'تصویر پروفایل',
        upload_to='avatars/',
        blank=True,
        null=True
    )
    bio = models.TextField('بیوگرافی', blank=True)
    
    is_active = models.BooleanField('فعال', default=True)
    is_staff = models.BooleanField('مدیر', default=False)
    
    date_joined = models.DateTimeField('تاریخ عضویت', auto_now_add=True)
    updated_at = models.DateTimeField('آخرین بروزرسانی', auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name or self.username