# Generated by Django 4.2 on 2023-04-18 18:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_carouselmodel_descriptions_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='faqmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='faqmodel',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='faqmodel',
            name='title_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='individualcreditmodel',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='individualcreditmodel',
            name='description_uz',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='individualcreditmodel',
            name='title_ru',
            field=models.CharField(max_length=400, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='individualcreditmodel',
            name='title_uz',
            field=models.CharField(max_length=400, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='individualcredittypemodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='individualcredittypemodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='individualcredittypemodel',
            name='title_ru',
            field=models.CharField(max_length=400, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='individualcredittypemodel',
            name='title_uz',
            field=models.CharField(max_length=400, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]
