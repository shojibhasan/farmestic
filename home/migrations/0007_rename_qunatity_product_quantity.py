# Generated by Django 3.2.9 on 2021-12-02 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_qunatity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
