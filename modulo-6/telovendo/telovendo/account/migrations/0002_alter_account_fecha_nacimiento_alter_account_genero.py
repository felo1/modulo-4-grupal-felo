# Generated by Django 4.2.2 on 2023-06-08 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='genero',
            field=models.CharField(choices=[('m', 'f'), ('f', 'm'), ('o', 'o')], max_length=6),
        ),
    ]