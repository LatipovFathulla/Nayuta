# Generated by Django 4.2 on 2023-04-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_legalentitiesmodel_first_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='payment_schedule',
            field=models.CharField(choices=[('annuity', 'Annuity'), ('differentiated', 'Differentiated')], max_length=20),
        ),
    ]
