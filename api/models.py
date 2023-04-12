from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


# Carousel Model
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


# End Carouserl Model

# Calculator Model
class CalculatorModel(models.Model):
    BORROW_CHOICES = (
        ('физическим лицам', 'Физическим лицам'),
        ('юридическим лицам', 'Юридическим лицам'),
    )
    borrower_type = models.CharField(
        max_length=70,
        choices=BORROW_CHOICES,
        default=BORROW_CHOICES[0],
        null=True,
        blank=True,
        verbose_name=_('borrower_type'))
    loan_amount = models.FloatField(verbose_name=_('loan_amount'))
    loan_term = models.IntegerField(verbose_name=_('loan_term'))
    interest_rate = models.FloatField(verbose_name=_('interest_rate'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.borrower_type

    class Meta:
        verbose_name = _('Calculator')
        verbose_name_plural = _('Calculators')


class ProductModel(models.Model):
    image = models.FileField(upload_to='ProductImage', verbose_name=_('image'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    link = models.URLField(verbose_name=_('link'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Product')


class FAQModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
