# Generated by Django 5.2 on 2025-05-02 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory', '0002_alter_category_image'),
        ('product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagoryid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catagory.category'),
            preserve_default=False,
        ),
    ]
