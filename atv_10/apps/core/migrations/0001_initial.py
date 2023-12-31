# Generated by Django 4.2.6 on 2023-10-05 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(max_length=400, verbose_name='Descrição')),
                ('label', models.CharField(max_length=50, verbose_name='Selo')),
                ('year', models.PositiveIntegerField(default=2023, verbose_name='Ano')),
                ('country', models.CharField(max_length=100, verbose_name='País')),
                ('gender', models.CharField(max_length=1, verbose_name='Genero')),
                ('qtd', models.PositiveIntegerField(default=0, verbose_name='Quantidade')),
            ],
        ),
    ]
