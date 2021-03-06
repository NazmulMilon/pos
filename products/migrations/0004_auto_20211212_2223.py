# Generated by Django 3.2.8 on 2021-12-12 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20211212_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='origin',
            name='origin_name',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='products.origin'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='products.seller'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_name',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
