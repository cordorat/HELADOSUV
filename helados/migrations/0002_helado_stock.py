# Generated by Django 5.1.3 on 2024-12-05 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='helado',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
