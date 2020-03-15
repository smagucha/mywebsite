# Generated by Django 2.1.7 on 2020-03-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualityofitem', models.CharField(max_length=30)),
                ('numberofitem', models.IntegerField()),
                ('expirydate', models.CharField(max_length=30)),
                ('officer', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'newstock',
                'permissions': [('Can_view_newstock', 'view newstock'), ('Can_add_newstock', 'add entry to the newstock'), ('Can_change_newstock', 'Can change data in newstock'), ('Can_delete_newstock', 'Can remove data innewstock')],
            },
        ),
    ]
