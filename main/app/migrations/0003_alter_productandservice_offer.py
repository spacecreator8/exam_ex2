# Generated by Django 5.0 on 2023-12-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_productandservice_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productandservice',
            name='offer',
            field=models.BooleanField(choices=[(0, 'Товар'), (1, 'Услуга')], default=0),
        ),
    ]
