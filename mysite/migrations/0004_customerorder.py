# Generated by Django 2.1.7 on 2019-11-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20191115_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberofitem', models.IntegerField()),
            ],
        ),
    ]