# Generated by Django 4.0.4 on 2022-06-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namche', '0015_remove_booking_adult_remove_booking_date_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adult',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='roomname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
