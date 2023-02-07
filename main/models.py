from django.db import models
from django.forms import ModelForm

# Create your models here.
class Task(models.Model):
    MONTH_CHOICE = (
        ('JA', 'Январь'),
        ('FE', 'Февраль'),
        ('MR', 'Март'),
        ('AP', 'Апрель'),
        ('MY', 'Май'),
        ('JN', 'Июнь'),
        ('JL', 'Июль'),
        ('AU', 'Август'),
        ('SP', 'Сентябрь'),
        ('OC', 'Октябрь'),
        ('NV', 'Ноябрь'),
        ('DC', 'Декабрь'),
    )

    DIFF = (
        ('ST','легкая задача'),
        ('CT','комплесный план'),
    )

    month = models.CharField(max_length=2, 
                             choices=MONTH_CHOICE,
                             default="JA",
                             verbose_name="месяц")
    day = models.PositiveSmallIntegerField(verbose_name="день(число)")
    difficulty = models.CharField(max_length=2,
                                  choices=DIFF,
                                  default='ST',
                                  verbose_name="сложность")
    title = models.CharField(max_length=100, verbose_name="название или простое описание")
    body = models.TextField(blank=True, verbose_name="более подробное и длинное описание")
    file = models.FileField(blank=True, verbose_name="изображение (если необходимо)")

    class Meta:
        verbose_name = "Сложность, дата"
        verbose_name_plural = "Сложность и даты"

    def __str__(self):
        return f"{self.title}, {self.difficulty}"
    
    