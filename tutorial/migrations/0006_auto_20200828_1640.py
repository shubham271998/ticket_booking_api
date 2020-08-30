# Generated by Django 3.1 on 2020-08-28 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_auto_20200828_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='tutorial.movie'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='tutorial.user'),
        ),
    ]
