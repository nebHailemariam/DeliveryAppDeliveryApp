# Generated by Django 2.2.12 on 2020-05-13 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200508_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(max_length=30)),
                ('sub_city', models.TextField(max_length=30)),
                ('postcode', models.CharField(max_length=5)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Location')),
            ],
        ),
    ]