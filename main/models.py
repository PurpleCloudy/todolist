from django.db import models

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
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    img = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Сложность, дата"
        verbose_name_plural = "Сложность и даты"

    def __str__(self):
        return f"{self.difficulty}, {self.day} {self.month}"