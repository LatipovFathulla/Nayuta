# Generated by Django 4.2 on 2023-09-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_japanesecarouselmodel_japanesepdf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='japanesecarouselmodel',
            name='descriptions_ru',
            field=models.TextField(blank=True, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='japanesecarouselmodel',
            name='descriptions_uz',
            field=models.TextField(blank=True, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='japanesecarouselmodel',
            name='title_ru',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='japanesecarouselmodel',
            name='title_uz',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='japaneseproductmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='japaneseproductmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='japaneseproductmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='japaneseproductmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='japaneseteammodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='descriptions team'),
        ),
        migrations.AddField(
            model_name='japaneseteammodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='descriptions team'),
        ),
        migrations.AddField(
            model_name='japaneseteammodel',
            name='name_ru',
            field=models.CharField(max_length=60, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='japaneseteammodel',
            name='name_uz',
            field=models.CharField(max_length=60, null=True, verbose_name='name'),
        ),
    ]
