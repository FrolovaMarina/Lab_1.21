from django.db import models


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    anons = models.CharField('Анонс', max_length=300)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата'),
    null = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
