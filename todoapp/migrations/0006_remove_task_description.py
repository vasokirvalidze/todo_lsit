# Generated by Django 4.2.16 on 2024-12-04 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_task_description_alter_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
