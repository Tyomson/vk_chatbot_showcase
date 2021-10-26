import keyboard_settings


SCENARIOS = {
    'views_goods': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Выберите что вас интересует',
                'keyboard': keyboard_settings.keyboard_1.get_keyboard(),
                'handler': 'handler_step1',
                'next_step': ['tires', 'avtodiski'],
                'previous_step': None
            },
            'tires': {
                'text': 'Выберите производителя Автошин',
                'keyboard': keyboard_settings.keyboard_2.get_keyboard(),
                'handler': 'handler_manufacture',
                'next_step': 'carousel',
                'previous_step': 'step1',
            },
            'avtodiski': {
                'text': 'Выберите производителя Автодисков',
                'keyboard': keyboard_settings.keyboard_3.get_keyboard(),
                'handler': 'handler_manufacture',
                'next_step': 'carousel',
                'previous_step': 'step1',
            },
            'carousel': {
                'text': 'Доступные товары',
                'keyboard': None,
                'handler': 'handler_carousel',
                'next_step': None,
                'previous_step': 'step1',
            }
        }
    }
}



