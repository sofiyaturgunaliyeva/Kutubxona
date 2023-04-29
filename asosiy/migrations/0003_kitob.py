# Generated by Django 4.2 on 2023-04-15 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_muallif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('sahifa', models.SmallIntegerField()),
                ('janr', models.CharField(max_length=50)),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.muallif')),
            ],
        ),
    ]