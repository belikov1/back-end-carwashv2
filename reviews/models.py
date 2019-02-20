from django.db import models


class ReviewsModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=300, verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзывы'
