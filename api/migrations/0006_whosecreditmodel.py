# Generated by Django 4.2 on 2023-04-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_faqmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoseCreditModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='title')),
                ('subtitle', models.CharField(max_length=400, verbose_name='subtitle')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Who can get a loan?',
                'verbose_name_plural': 'Who can get a loan?',
            },
        ),
    ]
