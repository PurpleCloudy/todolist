from django.db import models
from django.forms import ModelForm

# Create your models here.
class Task(models.Model):
    MONTH_CHOICE = (
        ('1', 'Январь'),
        ('2', 'Февраль'),
        ('3', 'Март'),
        ('4', 'Апрель'),
        ('5', 'Май'),
        ('6', 'Июнь'),
        ('7', 'Июль'),
        ('8', 'Август'),
        ('9', 'Сентябрь'),
        ('10', 'Октябрь'),
        ('11', 'Ноябрь'),
        ('12', 'Декабрь'),
    )

    DIFF = (
        ('ST','легкая задача'),
        ('CT','комплесный план'),
    )

    month = models.CharField(max_length=2, 
                             choices=MONTH_CHOICE,
                             default="1",
                             verbose_name="месяц")
    day = models.PositiveSmallIntegerField(verbose_name="день(число)")
    difficulty = models.CharField(max_length=2,
                                  choices=DIFF,
                                  default='ST',
                                  verbose_name="сложность")
    title = models.CharField(max_length=100, verbose_name="название или простое описание")
    body = models.TextField(blank=True, verbose_name="более подробное и длинное описание")
    file = models.FileField(upload_to='',blank=True, verbose_name="изображение или другой файл")

    class Meta:
        verbose_name = "Сложность, дата"
        verbose_name_plural = "Сложность и даты"

    def __str__(self):
        return f"{self.title}, {self.difficulty}"
    
    