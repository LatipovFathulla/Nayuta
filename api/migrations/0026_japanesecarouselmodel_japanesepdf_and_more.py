# Generated by Django 4.2 on 2023-09-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_credit_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='JapaneseCarouselModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=90, null=True)),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='descriptions')),
                ('image', models.FileField(upload_to='Carousel-images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Japanese Carousel',
                'verbose_name_plural': 'Japanese Carousels',
            },
        ),
        migrations.CreateModel(
            name='JapanesePDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='JapanesePDF', verbose_name='pdf')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Japanese PDF',
                'verbose_name_plural': 'Japanese PDF',
            },
        ),
        migrations.CreateModel(
            name='JapaneseProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='ProductJapanese', verbose_name='image')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Japanese Product',
                'verbose_name_plural': 'Japanese Products',
            },
        ),
        migrations.CreateModel(
            name='JapaneseTeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('description', models.TextField(verbose_name='descriptions team')),
                ('image', models.FileField(upload_to='JapaneseTeam')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Japanese Team',
                'verbose_name_plural': 'Japanese Teams',
            },
        ),
    ]
