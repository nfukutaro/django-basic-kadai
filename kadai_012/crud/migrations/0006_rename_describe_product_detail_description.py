# Generated by Django 5.1.1 on 2024-09-28 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_product_describe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='describe',
            new_name='detail_description',
        ),
    ]
