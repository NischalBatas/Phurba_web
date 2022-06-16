# Generated by Django 4.0.4 on 2022-06-16 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('namche', '0020_remove_booking_s_phone_alter_booking_uname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.BigIntegerField(null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='roomname',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='namche.room'),
        ),
    ]
