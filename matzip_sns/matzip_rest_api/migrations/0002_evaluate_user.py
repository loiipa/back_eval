# Generated by Django 3.2.8 on 2021-10-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matzip_rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluate',
            name='user',
            field=models.CharField(default='chjang', max_length=64),
        ),
    ]
