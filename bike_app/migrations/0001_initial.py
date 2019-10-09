# Generated by Django 2.2.5 on 2019-09-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rideData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('pickup', models.CharField(max_length=1000)),
                ('dropoff', models.CharField(max_length=1000)),
                ('stopovers', models.CharField(max_length=1000)),
                ('depart_time', models.DateTimeField()),
                ('return_time', models.DateTimeField(null=True)),
                ('is_return', models.BooleanField(default=False)),
            ],
        ),
    ]