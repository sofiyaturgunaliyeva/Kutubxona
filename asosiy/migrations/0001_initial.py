# Generated by Django 4.2 on 2023-04-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('kitob_soni', models.SmallIntegerField()),
                ('kurs', models.SmallIntegerField()),
            ],
        ),
    ]
