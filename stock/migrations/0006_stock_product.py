# Generated by Django 2.0.1 on 2020-09-11 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20200901_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.product'),
        ),
    ]