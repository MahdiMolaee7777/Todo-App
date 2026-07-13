from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('نام کاربری الزامی است')
        if not email:
            raise ValueError('ایمیل الزامی است')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser باید is_staff=True داشته باشد')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser باید is_superuser=True داشته باشد')
        
        return self.create_user(username, email, password, **extra_fields)