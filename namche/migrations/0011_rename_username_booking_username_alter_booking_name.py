# Generated by Django 4.0.4 on 2022-06-15 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('namche', '0010_booking_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Username',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='namche.room'),
        ),
    ]