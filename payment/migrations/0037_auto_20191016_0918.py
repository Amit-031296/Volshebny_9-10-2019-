# Generated by Django 2.2.1 on 2019-10-16 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0036_auto_20191016_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_address',
            field=models.CharField(blank=True, max_length=920),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_company_name',
            field=models.CharField(blank=True, max_length=920),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_email',
            field=models.CharField(blank=True, max_length=920),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_telephone',
            field=models.CharField(blank=True, max_length=920),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_website',
            field=models.CharField(blank=True, max_length=920),
        ),
    ]
