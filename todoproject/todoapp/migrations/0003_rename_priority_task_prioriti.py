# Generated by Django 4.2 on 2023-04-13 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='priority',
            new_name='prioriti',
        ),
    ]
