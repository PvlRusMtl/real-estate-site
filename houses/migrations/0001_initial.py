# Generated by Django 3.2.11 on 2022-01-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
    ]
