# Generated by Django 5.0 on 2023-12-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productandservice',
            name='offer',
            field=models.CharField(choices=[(0, 'Товар'), (1, 'Услуга')], default=0, max_length=100),
        ),
    ]
