# Generated by Django 3.2.23 on 2023-12-29 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0003_delete_itemcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='description',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='internal_company',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='original_order',
        ),
    ]