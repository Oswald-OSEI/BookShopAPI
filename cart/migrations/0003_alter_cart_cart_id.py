# Generated by Django 4.2.4 on 2023-10-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_book_cartitem_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.IntegerField(blank=True, max_length=250),
        ),
    ]
