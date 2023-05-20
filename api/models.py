from ckeditor.fields import RichTextField
from django.db import models

from modeltranslation.translator import TranslationOptions, translator
from django.utils.translation import gettext_lazy as _


# Carousel Model

class CarouselModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    image = models.FileField(upload_to='Carousel-images', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')


# End Carouserl Model

# Calculator Model
class Credit(models.Model):
    ANNUITY = 'annuity'
    DIFFERENTIATED = 'differentiated'

    PAYMENT_SCHEDULE_CHOICES = [
        (ANNUITY, 'Annuity'),
        (DIFFERENTIATED, 'Differentiated'),
    ]

    price = models.DecimalField(max_digits=15, decimal_places=2)
    down_payment_percentage = models.DecimalField(max_digits=6, decimal_places=2)
    loan_amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=15, decimal_places=2)
    payment_schedule = models.CharField(max_length=20, choices=PAYMENT_SCHEDULE_CHOICES)
    loan_period = models.IntegerField()
    pdf = models.FileField(upload_to='pdfs/',  null=True)

class Payment(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE, related_name='payments')
    payment_number = models.IntegerField()
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_amount = models.DecimalField(max_digits=12, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=12, decimal_places=2)


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


# Individual Credit Model
class IndividualCreditModel(models.Model):
    title = models.CharField(max_length=400, verbose_name=_('title'))
    description = RichTextField(verbose_name=_('description'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Individual Credit')
        verbose_name_plural = _('Individual Credits')


class IndividualCreditTypeModel(models.Model):
    title = models.CharField(max_length=400, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    first_image = models.FileField(upload_to='Individual-images', verbose_name=_('first_image'))
    second_image = models.FileField(upload_to='Individual-images', verbose_name=_('second_image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Type of loans')
        verbose_name_plural = _('Type of loans')


# Yuridik credit
# class LegalEntitiesModel(models.Model):
#     title = models.CharField(max_length=400, verbose_name=_('title'))
#     short_description = models.TextField(verbose_name=_('description'))
#     long_description = RichTextField(verbose_name=_('long_description'))
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = _('Legal Entities')
#         verbose_name_plural = _('Legal Entities')


class LegalEntitiesModel(models.Model):
    title = models.CharField(max_length=400, verbose_name=_('title'))
    short_description = models.TextField(verbose_name=_('description'))
    long_description = RichTextField(verbose_name=_('long_description'))
    first_image = models.FileField(upload_to='Individual-images', verbose_name=_('first_image'))
    second_image = models.FileField(upload_to='Individual-images', verbose_name=_('second_image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Legal Entities')
        verbose_name_plural = _('Legal Entities')
