# Generated by Django 2.0 on 2017-12-29 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0002_auto_20171230_1029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Database_meals',
            new_name='meals_local_db',
        ),
    ]