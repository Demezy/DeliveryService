# Generated by Django 3.1.2 on 2020-10-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.CharField(blank=True, max_length=100, verbose_name='img'),
        ),
    ]