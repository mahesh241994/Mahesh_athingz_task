# Generated by Django 4.2.22 on 2025-06-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskapp', '0002_alter_salesrecord_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrecord',
            name='order_id',
            field=models.IntegerField(unique=True),
        ),
    ]
