# Generated by Django 3.1.2 on 2020-10-25 18:11

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0007_auto_20201025_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='invitation_code',
        ),
        migrations.AddField(
            model_name='courier',
            name='invitation_code',
            field=models.TextField(default=main.models.pass_gen, verbose_name='invitation_code'),
        ),
    ]
