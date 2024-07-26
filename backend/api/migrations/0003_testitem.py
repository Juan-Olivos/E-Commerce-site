# Generated by Django 5.0.3 on 2024-07-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_rename_item_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
        ),
    ]