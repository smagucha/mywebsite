# Generated by Django 2.0.1 on 2020-10-16 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_remove_sale_stockavailable'),
    ]

    operations = [
        migrations.CreateModel(
            name='mm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
