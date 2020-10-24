# Generated by Django 3.1.2 on 2020-10-23 22:24

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KodeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='email')),
                ('password', models.TextField(blank=True, verbose_name='password')),
                ('invitation_code', models.TextField(default=main.models.pass_gen, verbose_name='invitation_code')),
            ],
        ),
    ]
