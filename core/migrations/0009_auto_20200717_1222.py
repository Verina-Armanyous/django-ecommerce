# Generated by Django 2.2.14 on 2020-07-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_item_org_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('B', 'Billing')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('A', 'Animals'), ('Ed', 'Education'), ('En', 'Environment'), ('H', 'Health'), ('HS', 'Human Services'), ('AC', 'Arts, Culture, and Humanities')], max_length=2),
        ),
    ]
