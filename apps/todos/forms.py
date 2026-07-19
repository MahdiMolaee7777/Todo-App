from django import forms
from .models import Todo, Category
import jdatetime


class TodoForm(forms.ModelForm):

    due_date = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'data-jdp': '',
                'autocomplete': 'off',
                'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg',
                'placeholder': 'انتخاب تاریخ',
            }
        )
    )

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

            'completed': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.instance.pk and self.instance.due_date:
            jalali_date = jdatetime.date.fromgregorian(
                date=self.instance.due_date
            )
            self.initial["due_date"] = jalali_date.strftime("%Y/%m/%d")

        if user:
            self.fields["category"].queryset = Category.objects.filter(user=user)

    def clean_due_date(self):
        value = self.cleaned_data.get("due_date")

        if not value:
            return None

        try:
            year, month, day = map(int, value.split("/"))
            return jdatetime.date(year, month, day).togregorian()
        except Exception:
            raise forms.ValidationError("فرمت تاریخ نامعتبر است.")


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