# Generated by Django 2.2.5 on 2020-02-21 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('img', models.ImageField(upload_to='pics')),
                ('Author', models.CharField(max_length=50)),
                ('desc', models.TextField(verbose_name='')),
                ('bookType', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
    ]
