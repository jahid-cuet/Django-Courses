# Generated by Django 5.0.1 on 2024-03-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='Rahim'),
        ),
    ]
