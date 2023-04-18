# Generated by Django 4.2 on 2023-04-18 17:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_legalentitiesmodel_long_description_ru_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WhoseCreditModel',
        ),
        migrations.AlterModelOptions(
            name='individualcreditmodel',
            options={'verbose_name': 'Individual Credit', 'verbose_name_plural': 'Individual Credits'},
        ),
        migrations.RemoveField(
            model_name='individualcreditmodel',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='individualcreditmodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='individualcreditmodel',
            name='title',
            field=models.CharField(default=1, max_length=400, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='individualcreditmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='created_at'),
        ),
    ]
