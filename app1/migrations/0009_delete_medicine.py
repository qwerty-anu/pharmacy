# Generated by Django 4.0.3 on 2022-04-12 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_medicine_id_medicine_medi_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicine',
        ),
    ]
