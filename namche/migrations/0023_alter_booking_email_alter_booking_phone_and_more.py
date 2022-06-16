# Generated by Django 4.0.4 on 2022-06-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namche', '0022_delete_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='uname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
