# Generated by Django 3.1.2 on 2020-10-28 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.PositiveIntegerField(choices=[(0, 'Courier'), (1, 'Manager')], default=0, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='main.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='district'),
        ),
    ]
