# Generated by Django 2.2.5 on 2020-02-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalSpectrum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sensor', models.ManyToManyField(blank=True, related_name='units', to='DigitalSpectrum.Sensor')),
            ],
        ),
    ]