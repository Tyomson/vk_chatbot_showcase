from peewee import *

db = SqliteDatabase('vk_bot.db')


class CategoryModel(Model):
    """Таблица с раделами"""
    category = CharField(
        verbose_name='категория',
        max_length=10,
        null=True,
        default=None
    )

    class Meta:
        database = db


class ManufacturerModel(Model):
    """Таблица с производителями"""
    manufacturer = CharField(
        verbose_name='производитель',
        max_length=20,
        null=True,
        default=None
    )
    category = ForeignKeyField(
        CategoryModel,
        backref='category',
        verbose_name='категория'
    )

    class Meta:
        database = db


class Goods(Model):
    """Таблица с товарами"""
    category = ForeignKeyField(
        CategoryModel,
        verbose_name='категория',
        related_name='goods_category'
    )
    manufacturer = ForeignKeyField(
        ManufacturerModel,
        backref='manufacturer',
        verbose_name='производитель',
        related_name='goods_manufacturer'
    )
    name = CharField(
        index=True,
        verbose_name='название товара',
        max_length=80
    )
    description = CharField(
        verbose_name='описнаие',
        max_length=80
    )
    img = TextField(
        verbose_name='путь до изображения'
    )

    class Meta:
        database = db


class UserState(Model):
    """Состояние пользователя внутри сценария."""
    user_id = CharField(
        verbose_name='Ид юзера'
    )
    scenario_name = CharField(
        verbose_name='название сценария'
    )
    step_name = CharField(
        verbose_name='название шага'
    )
    carousel_manufacturer = CharField(
        null=True, default=None
    )

    class Meta:
        database = db
