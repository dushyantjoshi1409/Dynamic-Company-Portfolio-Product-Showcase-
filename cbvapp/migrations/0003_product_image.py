# Generated by Django 5.0.8 on 2024-09-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cbvapp", "0002_alter_product_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="product_images/"),
        ),
    ]
