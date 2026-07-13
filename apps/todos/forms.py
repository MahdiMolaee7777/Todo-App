from django import forms
from .models import Todo, Category


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title',
            'description',
            'priority',
            'category',
            'due_date',
            'completed'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'عنوان کار'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'توضیحات (اختیاری)'
                }
            ),

            'priority': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'category': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'due_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),

            'completed': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['due_date'].input_formats = [
            '%Y-%m-%d'
        ]

        if user:
            self.fields['category'].queryset = Category.objects.filter(
                user=user
            )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نام دسته‌بندی'
                }
            ),

            'color': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'color'
                }
            ),
        }