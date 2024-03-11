from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def reply_to_message_ikb(user_id) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    
    ikb.button(text='Відповісти📩', callback_data=f'reply-to_{user_id}')
    ikb.adjust(1)
    
    return ikb.as_markup()


def abort_send_ansver() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    
    ikb.button(text='❌Відміна', callback_data=f'abort-reply-to')
    ikb.adjust(1)
    
    return ikb.as_markup()
