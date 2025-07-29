from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    details = models.TextField(verbose_name="جزئیات")
    is_completed = models.BooleanField(
        default=False, verbose_name='وضعیت انجام')
    created_at = jmodels.jDateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد')
    deadline = jmodels.jDateTimeField(verbose_name='تاریخ پایان')

    def __str__(self):
        return self.title
