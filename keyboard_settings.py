from vk_api.keyboard import VkKeyboard, VkKeyboardColor

import settings

# Клавиатура 1 с выбором автошин/дисков
keyboard_1 = VkKeyboard(**settings.SETTINGS_KEYBOARD)
keyboard_1.add_callback_button(label='Автошины', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "tires"})
keyboard_1.add_callback_button(label='Диски', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "avtodiski"})

# Клавиатура 2 с выбором 3-4 раздела в автошинах
keyboard_2 = VkKeyboard(**settings.SETTINGS_KEYBOARD)
keyboard_2.add_callback_button(label='Toyo', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "toyo"})
keyboard_2.add_callback_button(label='Continental', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "continental"})
keyboard_2.add_callback_button(label='Dunlop', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "dunlop"})
keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE,
                               payload={"type": "back"})

# Клавиатура 3 с выбором 3-4 раздела в дисках
keyboard_3 = VkKeyboard(**settings.SETTINGS_KEYBOARD)
keyboard_3.add_callback_button(label='Rial', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "rial"})
keyboard_3.add_callback_button(label='K&K', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "k&k"})
keyboard_3.add_callback_button(label='COX', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "cox"})
keyboard_3.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE,
                               payload={"type": "back"})

