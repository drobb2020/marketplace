# Generated by Django 5.0.2 on 2024-02-18 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ("-created_at",)},
        ),
    ]
