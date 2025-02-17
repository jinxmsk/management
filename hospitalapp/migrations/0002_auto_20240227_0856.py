# Generated by Django 3.2.24 on 2024-02-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('product_price', models.CharField(max_length=100)),
                ('product_quantity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
