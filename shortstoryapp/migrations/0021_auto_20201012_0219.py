# Generated by Django 3.1.2 on 2020-10-11 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortstoryapp', '0020_story_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='liked',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
