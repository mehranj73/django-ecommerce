# Generated by Django 3.1 on 2021-02-02 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product', '0003_auto_20201229_0922'),
        ('eshop_attribute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attrproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attrs', to='eshop_product.product', verbose_name='تگ'),
        ),
    ]
