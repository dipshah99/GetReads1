# Generated by Django 3.0.4 on 2020-03-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='products',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated',
        ),
        migrations.AddField(
            model_name='cart',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='orderId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
