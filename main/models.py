from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField('Название',
                             max_length=50)  # 1поле  с текстсом до 255 символом     Название - наименование поля  max_length=50 - мак число символов, которое моежно записать в поле
    task = models.TextField('Описание')  # TextField - поле для большого текста

    # Метод вызывается, когда вызывается объект данного класса на экран

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
