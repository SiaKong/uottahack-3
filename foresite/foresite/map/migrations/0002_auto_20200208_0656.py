# Generated by Django 3.0.2 on 2020-02-08 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='groupname',
        ),
    ]
