# Generated by Django 5.0.3 on 2024-07-27 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_order_is_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="api.product"
            ),
        ),
    ]