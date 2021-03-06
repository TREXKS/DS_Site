# Generated by Django 2.2.5 on 2019-12-03 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('function', models.CharField(max_length=200)),
                ('model_number', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(max_length=64)),
                ('weight', models.CharField(max_length=64)),
                ('warrenty', models.CharField(max_length=64)),
                ('manufacturer', models.CharField(max_length=64)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalSpectrum.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ManyToManyField(blank=True, related_name='checked_items', to='DigitalSpectrum.Cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_item',
            field=models.ManyToManyField(blank=True, related_name='cart_item', to='DigitalSpectrum.Sensor'),
        ),
    ]
