# Generated by Django 3.2.6 on 2021-08-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('seed', '0003_alter_seed_uniqueid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seed',
            name='sowing_months',
        ),
        migrations.AddField(
            model_name='seed',
            name='sowing_months',
            field=models.ManyToManyField(blank=True, to='core.Month', verbose_name='Sowing months'),
        ),
    ]
