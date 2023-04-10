from django.db import models
from django.utils.translation import gettext_lazy as _


class CarouselModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    image = models.FileField(upload_to='Carousel-images', verbose_name=_('image'))
    link = models.URLField(verbose_name=_('link'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')
