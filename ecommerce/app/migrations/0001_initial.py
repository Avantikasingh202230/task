# Generated by Django 3.2.16 on 2022-11-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('G', 'Grocery'), ('G', 'Mobiles'), ('G', 'Fashion'), ('G', 'Electronics'), ('G', 'Home'), ('G', 'Personal Care'), ('G', 'Appliances'), ('G', 'Toys and Baby'), ('G', 'Sports'), ('G', 'Bikes and Cars')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
