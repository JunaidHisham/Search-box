# Generated by Django 4.0.4 on 2022-05-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_alter_wordmeaning_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmeaning',
            name='meaning',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wordmeaning',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
