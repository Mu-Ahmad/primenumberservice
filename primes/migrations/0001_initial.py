# Generated by Django 4.2 on 2023-05-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CPUMemoryUsageLog",
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
                ("timestamp", models.DateTimeField()),
                ("cpu_usage", models.FloatField()),
                ("memory_usage", models.FloatField()),
            ],
        ),
    ]
