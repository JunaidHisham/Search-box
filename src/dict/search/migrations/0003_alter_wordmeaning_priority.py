# Generated by Django 4.0.4 on 2022-05-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_wordmeaning_meaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmeaning',
            name='priority',
            field=models.TextField(default=''),
        ),
    ]
