# Generated by Django 3.2.6 on 2021-08-26 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seed',
            old_name='sun_requirement',
            new_name='sun_needed',
        ),
    ]
