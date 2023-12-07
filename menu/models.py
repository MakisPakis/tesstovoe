from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    position = models.PositiveIntegerField('Позиция', default=1)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

