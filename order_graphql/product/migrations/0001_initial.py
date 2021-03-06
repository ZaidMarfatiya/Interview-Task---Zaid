# Generated by Django 4.0.5 on 2022-07-03 05:44

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
                ('category', models.CharField(max_length=200, null=True)),
                ('brand', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('imageurl', models.ImageField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(null=True)),
                ('placed', models.BooleanField(default=False)),
                ('total_price', models.IntegerField(null=True)),
                ('total_quantity', models.IntegerField(null=True)),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
    ]
