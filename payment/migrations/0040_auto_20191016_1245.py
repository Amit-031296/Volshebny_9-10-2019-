# Generated by Django 2.2.1 on 2019-10-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0039_allservices_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(choices=[('Air Ticket Service', 'Air Ticket Service'), ('Visa Cost Service', 'Visa Cost Service'), ('Hotel Quatation Service', 'Hotel Quatation Service'), ('Restuarant Quatation Service', 'Restuarant Quatation Service'), ('Entrances Quatation Service', 'Entrances Quatation Service'), ('SapSan Quatation Service', 'SapSan Quatation Service'), ('Guide Service', 'Guide Service'), ('Transport Service', 'Transport Service'), ('All Services', 'All Services')], default='Air Ticket Service', max_length=920),
        ),
    ]
