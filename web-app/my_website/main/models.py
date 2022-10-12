from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField('Назва',max_length=50,default='undefined')
    task = models.TextField("Текст завдання",default='undefined')
    answer = models.TextField("Відповідь",default='undefined')
    dateOfPublishing = models.DateField("Дата публікації",default='2022-09-12')
    level = models.TextField('Рівень складності',default='undefined')


    def __str__(self):
        return self.task_name


class SomeInfo(models.Model):
    name = models.CharField('Iм`я користувача',default='undefined',max_length=100)
    age = models.BigIntegerField('Вік',default=0,max_length=3)
    email = models.CharField('Email',default='undefined',max_length=150)
    phone = models.CharField('Телефон', default='undefined',max_length=15)
    HaveAuto = models.BooleanField('Має авто',default=0)

    def __str__(self):
        return self.name


