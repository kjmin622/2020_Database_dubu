# Generated by Django 3.0.6 on 2020-11-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_room_type_mem_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_info',
            name='card_number1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='card_info',
            name='card_number2',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='card_info',
            name='card_number3',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='card_info',
            name='card_number4',
            field=models.CharField(max_length=10),
        ),
    ]