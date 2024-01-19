# Generated by Django 4.2.6 on 2024-01-19 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Događaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('datum_i_vrijeme', models.DateTimeField()),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Volonter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=255)),
                ('prezime', models.CharField(max_length=255)),
                ('kontakt_email', models.EmailField(max_length=254)),
                ('kontakt_telefon', models.CharField(blank=True, max_length=15, null=True)),
                ('vjestine', models.TextField(blank=True, null=True)),
                ('interesi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.TextField()),
                ('organizator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.volonter')),
            ],
        ),
    ]