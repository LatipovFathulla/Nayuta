from ckeditor.fields import RichTextField
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


class WhoseCreditModel(models.Model):
    title = models.CharField(max_length=400, verbose_name=_('title'), null=True, blank=True)
    subtitle = models.CharField(max_length=400, verbose_name=_('subtitle'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Who can get a loan?')
        verbose_name_plural = _('Who can get a loan?')


class IndividualCreditModel(models.Model):
    title = models.CharField(max_length=400, verbose_name=_('title'), null=True, blank=True)
    subtitle = models.CharField(max_length=400, verbose_name=_('subtitle'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('What documents are needed?')
        verbose_name_plural = _('What documents are needed')


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
class LegalEntitiesModel(models.Model):
    title = models.CharField(max_length=400, verbose_name=_('title'))
    short_description = models.TextField(verbose_name=_('description'))
    long_description = RichTextField(verbose_name=_('long_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Legal Entities')
        verbose_name_plural = _('Legal Entities')
