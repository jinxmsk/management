# Generated by Django 3.2.24 on 2024-02-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('date', models.DateTimeField(null=True)),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
