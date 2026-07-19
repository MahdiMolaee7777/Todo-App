import jdatetime
from django import template

register = template.Library()


@register.filter(name='to_jalali')
def to_jalali(value, fmt="%Y/%m/%d"):
    """
    تبدیل تاریخ میلادی به شمسی
    استفاده: {{ todo.due_date|to_jalali }}
    یا با فرمت دلخواه: {{ todo.due_date|to_jalali:"%d %B %Y" }}
    """
    if not value:
        return ""
    jalali_date = jdatetime.date.fromgregorian(date=value)
    return jalali_date.strftime(fmt)