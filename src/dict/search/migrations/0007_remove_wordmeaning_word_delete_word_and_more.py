# Generated by Django 4.0.4 on 2022-05-22 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_wordmeaning_synonyms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordmeaning',
            name='word',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
        migrations.DeleteModel(
            name='WordMeaning',
        ),
    ]