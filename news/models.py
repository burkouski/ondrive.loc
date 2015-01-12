from django.db import models
from pytils import translit
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


class Category(models.Model):
    category = models.CharField('Категория', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = translit.slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:category_post_list', kwargs={'category_alias': self.alias})


class Post(models.Model):
    title = models.CharField('Заголовок статьи', max_length=200)
    alias = models.SlugField(max_length=100, blank=True)
    pub_date = models.DateField('Дата публикации')
    preview_img = models.ImageField('Превью изображение')
    preview = models.TextField('Вступительный текст')
    text = RichTextField('Полный текст')
    category = models.ForeignKey(Category)
    views = models.IntegerField('Количество просмотров')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = translit.slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:post_detail', kwargs={'post_alias': self.alias, 'category_alias': self.category.alias})


