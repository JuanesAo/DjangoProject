# Generated by Django 5.1.6 on 2025-03-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
