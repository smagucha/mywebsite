# Generated by Django 2.1.7 on 2020-03-02 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'permissions': [('Can_view_newstock', 'view newstock'), ('Can_add_newstock', 'add entry to the newstock'), ('Can_change_newstock', 'Can change data in newstock'), ('Can_delete_newstock', 'Can remove data innewstock')], 'verbose_name_plural': 'stock'},
        ),
    ]
