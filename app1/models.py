from django.db import models

class student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    std_number = models.IntegerField()
    TEACHER = (
        ('karbalaei','Karbalaei'),
        ('hasanzadeh','Hasanzadeh'),
        ('mohammadi','Mohammadi'),
    )
    teacher = models.CharField(max_length=15, choices=TEACHER, default='karbalaei')