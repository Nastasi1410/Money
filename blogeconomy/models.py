from django.db import models

# Create your models here.
class User (models.Model):

    CHOICE_Purpose = (
        ('Просто так','Simply'),
        ('Экономия','Economy'),
        ('Сбережение','Saving'),
    )
    Category_choice = (
        ('Студент','student'),
        ('Школьник','School'),
        ('Пенсионер','retiree'),
        ('Работаю','worked'),
    )


    Name=models.CharField(max_length=400)
    Category=models.CharField(max_length=400,choices=Category_choice)
    Purpose = models.CharField(max_length=400,choices=CHOICE_Purpose)
    Password=models.CharField(max_length=400)
    Salary=models.IntegerField()

class Mainclass(models.Model):
          ID_User=models.ForeignKey('User',on_delete = models.CASCADE)
          Categoryspend=models.CharField(max_length=400)
          Dateofspend=models.DateTimeField()
          Sum=models.IntegerField(default=0)

