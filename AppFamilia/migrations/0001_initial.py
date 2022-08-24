# Generated by Django 4.1 on 2022-08-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abuelos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('profesion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Padres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('profesion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Primos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('colorFavorito', models.CharField(max_length=40)),
            ],
        ),
    ]