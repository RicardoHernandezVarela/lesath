# Generated by Django 2.1.7 on 2019-12-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecg', '0017_auto_20191205_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='categoria',
            field=models.CharField(choices=[('Fonocardiograma', 'Fonocardiograma'), ('Electrocardiograma', 'Electrocardiograma'), ('Electromiograma', 'Electromiograma'), ('Oximetría', 'Oximetría'), ('Electrodérmica', 'Electrodérmica')], max_length=50),
        ),
    ]
