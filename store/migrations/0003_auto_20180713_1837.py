# Generated by Django 2.0 on 2018-07-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180713_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='cost_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]