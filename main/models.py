from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField('Title', max_length=100, unique=True)
    text = models.TextField('Main text')
    date = models.DateTimeField('Date', default=timezone.now)
    autor = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)

    views = models.IntegerField('Views', default=1)
    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    # )
    # shop_sizes = models.CharField(max_length=1, choices=sizes, default='S')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

