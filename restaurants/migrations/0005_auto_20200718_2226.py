# Generated by Django 2.2.12 on 2020-07-18 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_order_client_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='items',
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.DeliveryMan'),
        ),
    ]
