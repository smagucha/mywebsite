# Generated by Django 2.0.1 on 2020-11-08 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20201015_0815'),
        ('sales', '0014_delete_mm'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='stockavailable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='numberofitem1', to='stock.product'),
        ),
    ]