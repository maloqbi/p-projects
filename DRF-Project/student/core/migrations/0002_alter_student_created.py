# Generated by Django 4.0.5 on 2022-06-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
