# Generated by Django 4.2 on 2023-04-15 19:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_legalentitiesmodel_long_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalentitiesmodel',
            name='long_description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='legalentitiesmodel',
            name='long_description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='legalentitiesmodel',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='legalentitiesmodel',
            name='short_description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='legalentitiesmodel',
            name='title_ru',
            field=models.CharField(max_length=400, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='legalentitiesmodel',
            name='title_uz',
            field=models.CharField(max_length=400, null=True, verbose_name='title'),
        ),
    ]
