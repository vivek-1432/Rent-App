# Generated by Django 5.0.1 on 2024-01-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0002_prod_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]