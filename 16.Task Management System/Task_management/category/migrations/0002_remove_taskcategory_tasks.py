# Generated by Django 5.0.1 on 2024-03-16 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='tasks',
        ),
    ]