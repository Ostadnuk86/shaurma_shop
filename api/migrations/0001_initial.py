# Generated by Django 4.2.3 on 2023-07-22 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категории продуктов',
                'db_table': 'CategoryItems',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('tg_id', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Телеграмм ID')),
                ('phone_number', models.CharField(max_length=14, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'db_table': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220, verbose_name='Название продукта')),
                ('prise', models.CharField(max_length=10, verbose_name='Цена продукты')),
                ('composition', models.CharField(max_length=300, verbose_name='Состав продукта')),
                ('product_photo', models.ImageField(upload_to='product_photo/', verbose_name='Фото продукта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoryitems', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'db_table': 'Items',
            },
        ),
        migrations.CreateModel(
            name='ItemsOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=22, verbose_name='Кол-во продукта')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.items', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт/Заказ',
                'db_table': 'ItemsOrder',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'db_table': 'OrderStatus',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Способ оплаты')),
            ],
            options={
                'verbose_name': 'Способ оплаты',
                'db_table': 'PaymentMethod',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clients', verbose_name='Клиент')),
                ('items_in_order', models.ManyToManyField(through='api.ItemsOrder', to='api.items')),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.paymentmethod', verbose_name='Способ оплаты')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orderstatus', verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'Заказы',
                'db_table': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='itemsorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orders', verbose_name='Заказ'),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название адреса')),
                ('address', models.CharField(max_length=220, verbose_name='Адрес')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clients', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Адреса',
                'db_table': 'Addresses',
            },
        ),
    ]
