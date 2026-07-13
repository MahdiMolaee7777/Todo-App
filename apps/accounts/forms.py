from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    """فرم ثبت‌نام کاربر جدید با استایل Tailwind"""
    
    email = forms.EmailField(
        required=True,
        label='آدرس ایمیل',
        widget=forms.EmailInput(
            attrs={
                'class': 'block w-full pr-10 px-4 py-3.5 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all duration-200 placeholder-slate-400 font-medium shadow-sm',
                'placeholder': 'example@gmail.com'
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'نام کاربری',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'block w-full pr-10 px-4 py-3.5 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all duration-200 placeholder-slate-400 font-medium shadow-sm',
                    'placeholder': 'نام کاربری منحصر به فرد'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # استایل Tailwind برای فیلد رمز عبور اول
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password1'].widget.attrs.update({
            'class': 'block w-full pr-10 px-4 py-3.5 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all duration-200 placeholder-slate-400 font-medium shadow-sm',
            'placeholder': '••••••••'
        })
        
        # استایل Tailwind برای فیلد تکرار رمز عبور
        self.fields['password2'].label = 'تکرار رمز عبور'
        self.fields['password2'].widget.attrs.update({
            'class': 'block w-full pr-10 px-4 py-3.5 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all duration-200 placeholder-slate-400 font-medium shadow-sm',
            'placeholder': '••••••••'
        })


class UserLoginForm(AuthenticationForm):
    """فرم ورود کاربر با استایل Tailwind"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # استایل Tailwind برای فیلد نام کاربری
        self.fields['username'].label = 'نام کاربری یا ایمیل'
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full pr-10 px-4 py-3.5 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-primary-500/20 focus:border-primary-500 transition-all duration-200 placeholder-slate-400 font-medium shadow-sm',
            'placeholder': 'ایمیل یا نام کاربری خود را وارد کنید',
            'autofocus': True
        })
        
        # استایل Tailwind برای فیلد رمز عبور
        self.fields['password'].label = 'رمز عبور'
        self.fields['password'].widget.attrs.update({
            'class': 'block w-full pr-10 px-4 py-3.5 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-primary-500/20 focus:border-primary-500 transition-all duration-200 placeholder-slate-400 font-medium shadow-sm',
            'placeholder': 'رمز عبور خود را وارد کنید'
        })


class UserUpdateForm(forms.ModelForm):
    """فرم ویرایش پروفایل کاربر با استایل Tailwind"""
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'bio')
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'آدرس ایمیل',
            'avatar': 'تصویر پروفایل',
            'bio': 'درباره من'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'block w-full px-4 py-3 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-primary-500/20 focus:border-primary-500 transition-all duration-200 placeholder-slate-400 font-medium',
                    'placeholder': 'نام خود را وارد کنید'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'block w-full px-4 py-3 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-primary-500/20 focus:border-primary-500 transition-all duration-200 placeholder-slate-400 font-medium',
                    'placeholder': 'نام خانوادگی خود را وارد کنید'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'block w-full px-4 py-3 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-primary-500/20 focus:border-primary-500 transition-all duration-200 placeholder-slate-400 font-medium',
                    'placeholder': 'example@gmail.com'
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'block w-full px-4 py-3 text-slate-900 bg-slate-50 border-2 border-slate-200 rounded-xl focus:ring-4 focus:ring-primary-500/20 focus:border-primary-500 transition-all duration-200 placeholder-slate-400 font-medium resize-none',
                    'rows': 4,
                    'placeholder': 'چند خط درباره خودتان بنویسید...'
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2.5 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100 transition-all cursor-pointer',
                    'accept': 'image/*'
                }
            ),
        }