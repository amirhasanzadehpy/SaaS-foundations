# Generated by Django 5.0.8 on 2024-08-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_usersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
