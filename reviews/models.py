from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Review(models.Model):
    author = models.CharField('Автор', max_length=200)
    pub_date = models.DateField('Дата публикации')
    review = models.TextField('Отзыв')
    rate = models.PositiveIntegerField('Рейтинг')
    is_moderate = models.NullBooleanField("Прошел модерацию?", default=None)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
