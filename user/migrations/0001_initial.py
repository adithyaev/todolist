# Generated by Django 5.0 on 2023-12-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('completed_date', models.CharField(default='incomplete', max_length=20)),
                ('status', models.CharField(default='pending', max_length=10)),
            ],
        ),
    ]
