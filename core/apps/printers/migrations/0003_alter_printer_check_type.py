# Generated by Django 4.0.6 on 2022-07-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0002_alter_printer_options_alter_printer_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='check_type',
            field=models.CharField(choices=[('kitchen', 'kitchen'), ('client', 'client')], max_length=20, verbose_name='тип чека которые печатает принтер'),
        ),
    ]
