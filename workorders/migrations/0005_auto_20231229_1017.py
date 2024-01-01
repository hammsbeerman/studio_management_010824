# Generated by Django 3.2.23 on 2023-12-29 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customercontact_address1_customercontact_address2_and_more'),
        ('workorders', '0004_auto_20231229_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Category')),
                ('item_order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Display Order')),
                ('category', models.CharField(blank=True, max_length=100, null=True, verbose_name='Category')),
                ('original_item_order', models.CharField(blank=True, max_length=100, null=True, verbose_name='Original Item Order')),
                ('original_item_price', models.CharField(blank=True, max_length=100, null=True, verbose_name='Original Item Price')),
                ('internal_company', models.CharField(max_length=100, verbose_name='Internal Company')),
                ('workorder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workorders.workorder')),
            ],
        ),
    ]
