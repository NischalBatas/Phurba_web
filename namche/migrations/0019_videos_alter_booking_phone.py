# Generated by Django 4.0.4 on 2022-06-16 12:01

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namche', '0018_booking_s_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=500)),
                ('video', models.FileField(upload_to='videos/%y')),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.BigIntegerField(null=True, verbose_name=builtins.max),
        ),
    ]