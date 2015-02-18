from django.db import models

# Create your models here.
class Review(models.Model):
    author = models.CharField('Автор', max_length=200)
    pub_date = models.DateField('Дата публикации')
    review = models.TextField('Отзыв')
