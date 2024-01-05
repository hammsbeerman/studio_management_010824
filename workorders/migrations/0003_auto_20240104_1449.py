# Generated by Django 3.2.23 on 2024-01-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0002_remove_workorderitem_mark_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorderitem',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='workorderitem',
            name='total_price',
            field=models.IntegerField(verbose_name='Total Price'),
        ),
        migrations.AlterField(
            model_name='workorderitem',
            name='unit_price',
            field=models.IntegerField(verbose_name='Unit Price'),
        ),
    ]
