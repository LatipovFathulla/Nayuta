# Generated by Django 4.2 on 2023-04-15 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_legalentitiesmodel_long_description_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legalentitiesmodel',
            name='long_description_ru',
        ),
        migrations.RemoveField(
            model_name='legalentitiesmodel',
            name='long_description_uz',
        ),
        migrations.RemoveField(
            model_name='legalentitiesmodel',
            name='short_description_ru',
        ),
        migrations.RemoveField(
            model_name='legalentitiesmodel',
            name='short_description_uz',
        ),
        migrations.RemoveField(
            model_name='legalentitiesmodel',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='legalentitiesmodel',
            name='title_uz',
        ),
    ]