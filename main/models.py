from django.db import models

# Create your models here.
class Task(models.Model):
    DIFF = (
        ('ST','легкая задача'),
        ('CT','комплесный план'),
    )

    date = models.DateField()
    difficulty = models.CharField(max_length=2,
                                  choices=DIFF,
                                  default='ST',
                                  verbose_name="сложность")
    title = models.CharField(max_length=100, verbose_name="название или простое описание")
    body = models.TextField(blank=True, verbose_name="более подробное и длинное описание")
    img = models.ImageField(upload_to='staticbase/media',blank=True, verbose_name="изображение или другой файл")

    class Meta:
        verbose_name = "Сложность, дата"
        verbose_name_plural = "Сложность и даты"

    def __str__(self):
        return f"{self.title}, {self.difficulty}"
    
    