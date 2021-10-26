"""
Handler - функция, которая принимает на вход
    event: Событие пользователя VKBotMessageEvent object,
    step: Словарь текущего шага dict,
    state: SelectQuery,
    api: VkApiMethod,
    manufacturer: Производитель str
A возвращает либо карусель продуктов либо название шага предварительно сохранив его в базу
"""
import json

import requests

from models import Goods, ManufacturerModel


def handler_carousel(event, step, state, api, manufacturer):
    if event.object.payload:
        if event.object.payload.get('type') == 'back':
            step = step['previous_step']
            state.step_name = step
            state.save()
            return step
    carousel = {'type': 'carousel'}
    list_goods = []
    for goods in Goods.select().join(
            ManufacturerModel
    ).where(
        Goods.manufacturer.manufacturer == manufacturer
    ):
        tuple_goods = {}
        tuple_goods['title'] = goods.name
        tuple_goods['description'] = goods.description[:80]
        upload_url = api.photos.getMessagesUploadServer()['upload_url']
        with open(goods.img, 'rb') as img:
            upload_date = requests.post(
                upload_url,
                files={
                    'photo': (
                        'image.jpeg',
                        img,
                        'image/jpeg')
                }
            ).json()
        image_date = api.photos.saveMessagesPhoto(**upload_date)
        owner_id = image_date[0]['owner_id']
        media_id = image_date[0]['id']
        access_key = image_date[0]['access_key']
        attachment = f'{owner_id}_{media_id}_{access_key}'
        tuple_goods['photo_id'] = attachment
        tuple_goods['buttons'] = [{"action": {
            "type": "callback",
            "label": "Вернутся в меню",
            'payload': {"type": "back"}
        }}]
        list_goods.append(tuple_goods)
    carousel['elements'] = list_goods
    carousel = json.dumps(
        carousel,
        ensure_ascii=False
    ).encode('utf-8')
    carousel = str(carousel.decode('utf-8'))
    return carousel


def handler_step1(event, step, state, api, manufacturer):
    step = event.object.payload.get('type')
    state.step_name = step
    state.save()
    print(step)
    return step


def handler_manufacture(event, step, state, api, manufacturer):
    type = event.object.payload.get('type')
    if type == 'back':
        step = step['previous_step']
    elif ManufacturerModel.select().where(
            ManufacturerModel.manufacturer == type
    ):
        step = 'carousel'
        state.carousel_manufacturer = type
    state.step_name = step
    state.save()
    return step
