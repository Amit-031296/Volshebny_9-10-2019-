# Generated by Django 2.2.1 on 2019-10-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0031_visacostquatation_visacost_service_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visacostquatation',
            name='visacost_service_cost',
            field=models.FloatField(blank=True),
        ),
    ]
