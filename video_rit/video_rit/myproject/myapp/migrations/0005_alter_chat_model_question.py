# Generated by Django 3.2.4 on 2021-06-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210615_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_model',
            name='question',
            field=models.CharField(max_length=50),
        ),
    ]
