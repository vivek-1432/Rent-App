# Generated by Django 5.0.1 on 2024-01-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
