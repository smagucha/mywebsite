# Generated by Django 2.1.7 on 2019-12-30 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20191227_2228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerorder',
            options={'permissions': [('Can_view_customerorder', 'view customerorder'), ('Can_add_customerorder', 'add entry to the customerorder'), ('Can_change_customerorder', 'Can change data in customerorder'), ('Can_delete_customerorder', 'Can remove data in customerorder')]},
        ),
        migrations.AlterModelOptions(
            name='eventform',
            options={'permissions': [('Can_view_EVENTform', 'viewEVENTform'), ('Can_add_EVENTform', 'add entry to the EVENTform'), ('Can_change_EVENTform', 'Can change data in EVENTform'), ('Can_delete_EVENTform', 'Can remove data in EVENTform')]},
        ),
        migrations.AlterModelOptions(
            name='incoming_purchase',
            options={'permissions': [('Can_view_incoming_purchase', 'view incoming_purchase'), ('Can_add_incoming_purchase', 'add entry to the incoming_purchase'), ('Can_change_incoming_purchase', 'Can change data in incoming_purchase'), ('Can_delete_incoming_purchase', 'Can remove data in incoming_purchase')]},
        ),
        migrations.AlterModelOptions(
            name='mypost',
            options={'permissions': [('Can_view_my_post', 'view mypost'), ('Can_add_my_post', 'add entry to the mypost'), ('Can_change_my_post', 'Can change data in mypost'), ('Can_delete_my_post', 'Can remove data in mypost')]},
        ),
        migrations.AlterModelOptions(
            name='neworderux',
            options={'permissions': [('Can_view_neworderux', 'view neworderux'), ('Can_add_neworderux', 'add entry to the neworderux'), ('Can_change_neworderux', 'Can change data in neworderux'), ('Can_delete_neworderux', 'Can remove data in neworderux')]},
        ),
        migrations.AlterModelOptions(
            name='newstock',
            options={'permissions': [('Can_view_newstock', 'view newstock'), ('Can_add_newstock', 'add entry to the newstock'), ('Can_change_newstock', 'Can change data in newstock'), ('Can_delete_newstock', 'Can remove data innewstock')]},
        ),
        migrations.AlterModelOptions(
            name='salex',
            options={'permissions': [('Can_view_salex', 'view salex'), ('Can_add_salex', 'add entry to thesalex'), ('Can_change_salex', 'Can change data in salex'), ('Can_delete_salex', 'Can remove data in salex')]},
        ),
    ]
