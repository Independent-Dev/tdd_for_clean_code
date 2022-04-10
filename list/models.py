from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
    # 252페이지에는  list = models.ForeignKey(List, default=None)로 나와 있음.

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('id', )
        unique_together = ('list', 'text')

