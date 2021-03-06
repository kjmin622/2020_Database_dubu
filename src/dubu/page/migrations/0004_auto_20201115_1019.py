# Generated by Django 3.0.6 on 2020-11-15 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20201115_1008'),
    ]

    operations = [
        migrations.DeleteModel(
            name='coupon_list',
        ),
        migrations.AlterField(
            model_name='bill',
            name='booking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.booking'),
        ),
        migrations.AlterField(
            model_name='book_request',
            name='booking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.booking'),
        ),
        migrations.AlterField(
            model_name='customer_info',
            name='booking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.booking'),
        ),
        migrations.AlterField(
            model_name='customer_phone',
            name='booking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.customer_info'),
        ),
        migrations.AlterField(
            model_name='engineering_content',
            name='facility_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.engineering'),
        ),
        migrations.AlterField(
            model_name='in_storage',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.product'),
        ),
        migrations.AlterField(
            model_name='member_customer',
            name='booking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.customer_info'),
        ),
        migrations.AlterField(
            model_name='member_email',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.member_info'),
        ),
        migrations.AlterField(
            model_name='member_phone',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.member_info'),
        ),
        migrations.AlterField(
            model_name='product_price',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.product'),
        ),
        migrations.AlterField(
            model_name='staff_account',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.account_info'),
        ),
        migrations.AlterField(
            model_name='staff_account',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.staff'),
        ),
        migrations.AlterField(
            model_name='staff_address',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.staff_info'),
        ),
        migrations.AlterField(
            model_name='staff_info',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.staff'),
        ),
        migrations.AlterField(
            model_name='staff_phone',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.staff'),
        ),
    ]
