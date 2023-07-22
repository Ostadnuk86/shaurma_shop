from django.db import models


class Clients(models.Model):
    """Клиенты"""
    name = models.CharField('Имя', max_length=30)
    tg_id = models.CharField('Телеграмм ID', max_length=20, null=True, default=None, blank=True)
    phone_number = models.CharField('Номер телефона', max_length=14)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиенты'
        db_table = 'Clients'


class Addresses(models.Model):
    """Адреса клиентов"""
    client = models.ForeignKey('Clients', on_delete=models.CASCADE, verbose_name='Клиент')
    title = models.CharField('Название адреса', max_length=50)
    address = models.CharField('Адрес', max_length=220)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Адреса'
        db_table = 'Addresses'


class Orders(models.Model):
    """Заказы"""
    client = models.ForeignKey('Clients', on_delete=models.CASCADE, verbose_name='Клиент')
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, verbose_name='Статус заказа')
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name='Способ оплаты',blank=True, null=True)
    order_date = models.DateTimeField('Дата и время заказа', blank=True, null=True)
    items_in_order = models.ManyToManyField('Items', through='ItemsOrder')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказы'
        db_table = 'Orders'


class PaymentMethod(models.Model):
    """Способ оплаты"""
    title = models.CharField('Способ оплаты', max_length=70)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ оплаты'
        db_table = 'PaymentMethod'


class OrderStatus(models.Model):
    """Статус заказа"""
    title = models.CharField('Статус заказа', max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус заказа'
        db_table = 'OrderStatus'


class ItemsOrder(models.Model):
    """Смежная таблица Продукт/Заказ"""
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, verbose_name='Заказ')
    item = models.ForeignKey('Items', on_delete=models.CASCADE, verbose_name='Продукт')
    count = models.CharField('Кол-во продукта', max_length=22)

    class Meta:
        verbose_name = 'Продукт/Заказ'
        db_table = 'ItemsOrder'


class Items(models.Model):
    """Продукты"""
    title = models.CharField('Название продукта', max_length=220)
    prise = models.CharField('Цена продукты', max_length=10)
    composition = models.CharField('Состав продукта', max_length=300)
    product_photo = models.ImageField('Фото продукта', upload_to='product_photo/')
    category = models.ForeignKey('CategoryItems', on_delete=models.CASCADE, verbose_name='Категория продукта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        db_table = 'Items'


class CategoryItems(models.Model):
    """Категория продуктов"""
    title = models.CharField('Название категории', max_length=70)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории продуктов'
        db_table = 'CategoryItems'
