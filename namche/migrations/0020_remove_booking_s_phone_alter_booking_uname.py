# Generated by Django 4.0.4 on 2022-06-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namche', '0019_videos_alter_booking_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='s_phone',
        ),
        migrations.AlterField(
            model_name='booking',
            name='uname',
            field=models.CharField(max_length=100, null=True, verbose_name='Full Name'),
        ),
    ]