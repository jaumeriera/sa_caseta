# Generated by Django 3.2.6 on 2021-08-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0002_rename_sun_requirement_seed_sun_needed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='uniqueId',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Code'),
        ),
    ]
