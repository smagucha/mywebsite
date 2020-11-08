# Generated by Django 2.0.1 on 2020-09-01 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20200302_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stock.Category')),
            ],
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name_plural': 'stock'},
        ),
        migrations.RemoveField(
            model_name='stock',
            name='expirydate',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='officer',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='qualityofitem',
        ),
    ]