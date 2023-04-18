# Generated by Django 4.2 on 2023-04-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_delete_whosecreditmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselmodel',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='carouselmodel',
            name='descriptions_uz',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='carouselmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='carouselmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]
