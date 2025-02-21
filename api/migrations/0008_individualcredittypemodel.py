# Generated by Django 4.2 on 2023-04-14 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_individualcreditmodel_alter_whosecreditmodel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualCreditTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('first_image', models.FileField(upload_to='Individual-images', verbose_name='first_image')),
                ('second_image', models.FileField(upload_to='Individual-images', verbose_name='second_image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Type of loans',
                'verbose_name_plural': 'Type of loans',
            },
        ),
    ]
