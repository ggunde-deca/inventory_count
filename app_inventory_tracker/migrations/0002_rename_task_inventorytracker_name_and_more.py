# Generated by Django 5.0.3 on 2024-03-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_inventory_tracker", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="inventorytracker",
            old_name="task",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="inventorytracker",
            name="completed",
        ),
        migrations.RemoveField(
            model_name="inventorytracker",
            name="timestamp",
        ),
        migrations.RemoveField(
            model_name="inventorytracker",
            name="updated",
        ),
        migrations.RemoveField(
            model_name="inventorytracker",
            name="user",
        ),
        migrations.AddField(
            model_name="inventorytracker",
            name="count",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name="inventorytracker",
            name="url",
            field=models.URLField(blank=True),
        ),
    ]
