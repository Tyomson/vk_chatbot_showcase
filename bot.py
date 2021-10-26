import logging

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

from models import UserState
import settings
import intent_settings
import handlers

log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log', encoding='UTF-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Сценарий просмотра витрины автошин/дисков. 3-4 раздела, в каждом по 2-3 товара.
     У товара описание и фотография.
    use Python 3.8

    """

    def __init__(self, token, group_id):
        """
        @param token: секретный токен
        @param group_id: group id из группы vk
        """
        self.token = token
        self.group_id = group_id

        self.vk = vk_api.VkApi(token=token, api_version='5.124')
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Запуск бота """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as exc:
                log.exception(f'Ошибка в обработке события: {exc}')

    def on_event(self, event):
        """
        Если евент новое сообщение или клик по callback кнопке
        @param event: VKBotMessageEvent object
        @return: None
        """

        if event.type != VkBotEventType.MESSAGE_NEW \
                and event.type != VkBotEventType.MESSAGE_EVENT:
            log.info(f'пока не умеем обрабатывать события такого типа - {event.type}')
            return
        user_id = event.message.peer_id if event.type == VkBotEventType.MESSAGE_NEW \
            else event.object.peer_id

        state = UserState.select().where(UserState.user_id == str(user_id))

        try:
            if state[0].user_id:
                self._continue_scenario(user_id, event, state[0])
        except (AttributeError, IndexError) as exp:
            if 'callback' not in event.obj.client_info['button_actions']:
                print(f'Клиент {user_id} не поддерж. callback')
            self._start_scenario(user_id)

    def _continue_scenario(self, user_id, event, state):
        """
        Продолжаем сценарий на основе id пользователя и названия шага на котором находиться пользователь
        :param user_id: int
        :param event: Событие пользователя VKBotMessageEvent object
        :param state: SelectQuery
        :return: None
        """
        steps = intent_settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if event.type == VkBotEventType.MESSAGE_NEW:
            if state.step_name == 'carousel':
                self._send_carousel(
                    event, state, user_id, step,
                    state.carousel_manufacturer, handler
                )
            else:
                self._send_keyboard(user_id, step)
        else:
            step = handler(
                event, step, state,
                self.api, state.carousel_manufacturer
            )
            current_step = steps[step]
            if step == 'carousel':
                self._change_carousel(
                    event, step, state,
                    current_step, state.carousel_manufacturer
                )
            else:
                self._change_keyboard(event, current_step)

    def _change_carousel(self, event, current_step, state, step, manufacturer):
        """
        Изменяем сообщение на карусель продуктов
        :param event: Событие пользователя VKBotMessageEvent object
        :param step: Словарь текущего шага dict
        :param state: SelectQuery
        :param current_step: Название текущего шага str
        :param manufacturer: Производитель str
        :return:
        """
        carousel = handlers.handler_carousel(
            event, current_step, state,
            self.api, manufacturer
        )
        self.api.messages.edit(
            peer_id=event.obj.peer_id,
            message=step['text'],
            conversation_message_id=event.obj.conversation_message_id,
            template=carousel
        )

    def _change_keyboard(self, event, step):
        """
        Изменяем меню пользователя
        :param event: Событие пользователя VKBotMessageEvent object
        :param step: Словарь текущего шага dict
        :return:
        """
        self.api.messages.edit(
            peer_id=event.obj.peer_id,
            message=step['text'],
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=step['keyboard']
        )

    def _send_keyboard(self, user_id, step):
        """
        Отправляем меню пользователю
        :param user_id: int
        :param step: Словарь текущего шага dict
        :return:
        """
        self.api.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            peer_id=user_id,
            keyboard=step['keyboard'],
            message=step['text'])

    def _send_carousel(self, event, state, user_id, step, manufacturer, handler):
        """
        Отправляем пользователю карусель с товарами
        :param event: Событие пользователя VKBotMessageEvent object
        :param state: SelectQuery
        :param user_id: int
        :param step: Словарь текущего шага dict
        :param manufacturer: Производитель str
        :param handler: function
        :return:
        """
        carousel = handler(event, step, state, self.api, manufacturer)
        self.api.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            peer_id=user_id,
            template=carousel,
            message=step['text'])

    def _start_scenario(self, user_id):
        """
        Начинаем сценарий для новго пользователя
        :param user_id:
        :return:
        """
        scenario = intent_settings.SCENARIOS['views_goods']
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        self._send_keyboard(user_id, step)
        UserState.create(
            user_id=str(user_id),
            scenario_name='views_goods',
            step_name=first_step
        )


if __name__ == '__main__':
    bot = Bot(token=settings.TOKEN, group_id=settings.GROUP_ID)
    bot.run()
