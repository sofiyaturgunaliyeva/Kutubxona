# Generated by Django 4.2 on 2023-04-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('kitob_soni', models.SmallIntegerField()),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=50)),
                ('tirik', models.BooleanField()),
                ('tugilgan_yili', models.SmallIntegerField()),
            ],
        ),
    ]
