# Generated by Django 4.2 on 2023-04-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0007_remove_record_qaytargan_sana_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='qaytargan_sana',
            field=models.DateField(null=True),
        ),
    ]
