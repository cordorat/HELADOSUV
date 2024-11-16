# Generated by Django 5.1.3 on 2024-11-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('documento', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='helado',
            name='cantidad',
        ),
    ]
