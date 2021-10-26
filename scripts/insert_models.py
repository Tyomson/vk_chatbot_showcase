import os
from models import CategoryModel, ManufacturerModel, Goods, UserState

CategoryModel.create_table()
ManufacturerModel.create_table()
Goods.create_table()
UserState.create_table()

tires = CategoryModel.create(categorys='tires')
avtodiski = CategoryModel.create(category='avtodiski')

toyo = ManufacturerModel.create(manufacturer='toyo', category=tires)
dunlop = ManufacturerModel.create(manufacturer='dunlop', category=tires)
continental = ManufacturerModel.create(manufacturer='continental', category=tires)

k_k = ManufacturerModel.create(manufacturer='k&k', category=avtodiski)
cox = ManufacturerModel.create(manufacturer='cox', category=avtodiski)
rial = ManufacturerModel.create(manufacturer='rial', category=avtodiski)

toyo_goods_1 = Goods.create(
    category=tires, manufacturer=toyo,
    name='Toyo Observe Ice-Freezer 175:70 R14 84T зимняя',
    description='Сезонность - зимние, Шипы - есть, Тип зимних шин - для северной зимы',
    img=os.path.join(
        'files', 'tires', 'toyo',
        'Toyo Observe Ice-Freezer 175:70 R14 84T зимняя.jpg'
    )
)
toyo_goods_2 = Goods.create(
    category=tires, manufacturer=toyo,
    name='Toyo Observe GSi-6 205:60 R16 92H зимняя',
    description='Сезонность - зимние, Срок службы - 5 лет, Гарантийный срок - 1 г.',
    img=os.path.join(
        'files', 'tires', 'toyo',
        'Toyo Observe GSi-6 205:60 R16 92H зимняя.jpg'
    )
)
toyo_goods_3 = Goods.create(
    category=tires, manufacturer=toyo,
    name='Toyo Observe Ice-Freezer 175:70 R14 84T зимняя',
    description='Сезонность - зимние, Шипы - есть, Тип зимних шин - для северной зимы',
    img=os.path.join(
        'files', 'tires', 'toyo',
        'Toyo Observe Ice-Freezer 175:70 R14 84T зимняя.jpg'
    )
)

dunlop_goods_1 = Goods.create(
    category=tires, manufacturer=dunlop,
    name='Dunlop SP Winter ICE02 175:70 R14 84T зимняя',
    description='Сезонность - зимние, Шипы - есть, Тип зимних шин - для северной зимы',
    img=os.path.join(
        'files', 'tires', 'dunlop',
        'Dunlop SP Winter ICE02 175:70 R14 84T зимняя.jpg'
    )
)
dunlop_goods_2 = Goods.create(
    category=tires, manufacturer=dunlop,
    name='Dunlop Winter Maxx WM02 185:60 R14 84T зимняя',
    description='Сезонность - зимние, Тип зимних шин - для северной зимы',
    img=os.path.join(
        'files', 'tires', 'dunlop',
        'Dunlop Winter Maxx WM02 185:60 R14 84T зимняя.jpg'
    )
)
dunlop_goods_3 = Goods.create(
    category=tires, manufacturer=dunlop,
    name='Dunlop Winter Maxx SJ8 225:70 R15 100R зимняя',
    description='Сезонность - зимние, Тип зимних шин - для северной зимы',
    img=os.path.join(
        'files', 'tires', 'dunlop',
        'Dunlop Winter Maxx SJ8 225:70 R15 100R зимняя.jpg'
    )
)

continental_goods_1 = Goods.create(
    category=tires, manufacturer=continental,
    name='Continental ContiVikingContact 7 175:65 R14 86T зимняя',
    description='Сезонность - зимние, Назначение - для легкового автомобиля',
    img=os.path.join(
        'files', 'tires', 'continental',
        'Continental ContiVikingContact 7 175:65 R14 86T зимняя.jpg'
    )
)
continental_goods_2 = Goods.create(
    category=tires, manufacturer=continental,
    name='Continental PremiumContact 6 205:55 R16 91H летняя',
    description='Сезонность - летние, Рисунок протектора - асимметричный',
    img=os.path.join(
        'files', 'tires', 'continental',
        'Continental PremiumContact 6 205:55 R16 91H летняя.jpg'
    )
)
continental_goods_3 = Goods.create(
    category=tires, manufacturer=continental,
    name='Continental ContiWinterContact TS 860S 205:55 R16 91H зимняя',
    description='Сезонность - зимние',
    img=os.path.join(
        'files', 'tires', 'continental',
        'Continental ContiWinterContact TS 860S 205:55 R16 91H зимняя.jpg'
    )
)


k_k_goods_1 = Goods.create(
    category=avtodiski, manufacturer=k_k,
    name='Колесный диск K&K КС704 6.5х16:5х114.3 D60.1 ET45, 8.5 кг, Алмаз черный',
    description='Тип - литые, Материал - легкий сплав',
    img=os.path.join(
        'files', 'avtodiski', 'k&k',
        'Колесный диск K&K КС704 6.5х16:5х114.3 D60.1 ET45, 8.5 кг, Алмаз черный.jpg'
    )
)
k_k_goods_2 = Goods.create(
    category=avtodiski, manufacturer=k_k,
    name='Колесный диск K&K КС737 6.5х16:5х108 D63.35 ET50, 8 кг, сильвер',
    description='Тип - литые, Материал - легкий сплав',
    img=os.path.join(
        'files', 'avtodiski', 'k&k',
        'Колесный диск K&K КС737 6.5х16:5х108 D63.35 ET50, 8 кг, сильвер.jpg'
    )
)
k_k_goods_3 = Goods.create(
    category=avtodiski, manufacturer=k_k,
    name='Колесный диск K&K Samara 6х16:4х100 D54.1 ET49, сильвер SK',
    description='Тип - литые, Материал - легкий сплав',
    img=os.path.join(
        'files', 'avtodiski', 'k&k',
        'Колесный диск K&K Samara 6х16:4х100 D54.1 ET49, сильвер SK.jpg'
    )
)

cox_goods_1 = Goods.create(
    category=avtodiski, manufacturer=cox,
    name='Колесный диск COX D3370-540 9xR17:5x127 D71.5 ET-40',
    description='Цвет товара - зелeный, Количество в комплекте - 4 шт.',
    img=os.path.join(
        'files', 'avtodiski', 'cox',
        'Колесный диск COX D3370-540 9xR17:5x127 D71.5 ET-40.jpg'
    )
)
cox_goods_2 = Goods.create(
    category=avtodiski, manufacturer=cox,
    name='Колесный диск COX YA9550-568 9.5xR20:5x114.3 D73.1 ET33',
    description='Тип - литые, Цвет товара - черный',
    img=os.path.join(
        'files', 'avtodiski', 'cox',
        'Колесный диск COX YA9550-568 9.5xR20:5x114.3 D73.1 ET33.jpg'
    )
)
cox_goods_3 = Goods.create(
    category=avtodiski, manufacturer=cox,
    name='Колесный диск COX YA9550-565 9.5xR20:5x114.3 D73.1 ET33',
    description='Тип - литые, Цвет товар - серебристый',
    img=os.path.join(
        'files', 'avtodiski', 'cox',
        'Колесный диск COX YA9550-565 9.5xR20:5x114.3 D73.1 ET33.jpg'
    )
)

rial_goods_1 = Goods.create(
    category=avtodiski, manufacturer=rial,
    name='Колесный диск RIAL Kodiak 6х15:5х112 D57.1 ET47, graphite',
    description='Тип - литые, Материал - легкий сплав',
    img=os.path.join(
        'files', 'avtodiski', 'rial',
        'Колесный диск RIAL Kodiak 6х15:5х112 D57.1 ET47, graphite.jpg'
    )
)
rial_goods_2 = Goods.create(
    category=avtodiski, manufacturer=rial,
    name='Колесный диск RIAL X10 8х18:5х120 D72.6 ET34, polar silver',
    description='Тип - литые, Материал - легкий сплав',
    img=os.path.join(
        'files', 'avtodiski', 'rial',
        'Колесный диск RIAL X10 8х18:5х120 D72.6 ET34, polar silver.jpg'
    )
)
rial_goods_3 = Goods.create(
    category=avtodiski, manufacturer=rial,
    name='Колесный диск RIAL Arktis 7.5х17:5х114.3 D70.1 ET40, polar silver',
    description='Тип - литые, Материал - легкий сплав',
    img=os.path.join(
        'files', 'avtodiski', 'rial',
        'Колесный диск RIAL Arktis 7.5х17:5х114.3 D70.1 ET40, polar silver.jpg'
    )
)
