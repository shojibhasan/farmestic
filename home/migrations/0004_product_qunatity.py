# Generated by Django 3.2.9 on 2021-12-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qunatity',
            field=models.IntegerField(default=1),
        ),
    ]
