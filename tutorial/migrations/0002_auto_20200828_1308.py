# Generated by Django 3.1 on 2020-08-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rate_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
