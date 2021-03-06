# Generated by Django 4.0 on 2021-12-13 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('plate_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle', to='drivers.driver')),
            ],
        ),
    ]
