# Generated by Django 4.2 on 2024-02-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_booking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='booking_number',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='query',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
