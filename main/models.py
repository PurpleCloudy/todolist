from django.db import models

# Create your models here.
class ChoosingTask(models.Model):
    MONTH_CHOICE = (
        ('JA', 'January'),
        ('FE', 'February'),
        ('MR', 'March'),
        ('AP', 'April'),
        ('MY', 'May'),
        ('JN', 'June'),
        ('JL', 'July'),
        ('AU', 'August'),
        ('SP', 'September'),
        ('OC', 'October'),
        ('NV', 'November'),
        ('DC', 'December'),
    )

    DIFF = (
        ('ST','simple task'),
        ('CT','complex task'),
    )

    month = models.CharField(max_length=9, choices=MONTH_CHOICE, default="JANUARY")
    
    day = models.PositiveSmallIntegerField()

    difficulty = models.CharField(max_length=2, choices=DIFF, default='ST')    

