# Generated by Django 4.2.6 on 2023-11-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=50)),
                ('User_email', models.EmailField(max_length=254)),
                ('User_address', models.CharField(max_length=50)),
                ('User_qualification', models.TextField()),
            ],
        ),
    ]
