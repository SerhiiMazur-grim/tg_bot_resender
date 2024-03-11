from __future__ import annotations

from typing import Any, Final

from aiogram import Bot, F
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.methods import TelegramMethod
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from aiogram_i18n import I18nContext

from services.database import DBUser
from app.filters.admin_filter import IsAdminFilter
from app.state import AnswerToState
from app.keyboards.inline_kb import abort_send_ansver


router: Final[Router] = Router(name=__name__)


@router.callback_query(F.data.startswith('reply-to'))
async def answer_to_user(callback_query: CallbackQuery, bot: Bot,
                                   i18n: I18nContext, user: DBUser,
                                   state: FSMContext) -> None:
    await callback_query.answer()
    user_id = callback_query.data.split('_')[-1]
    await state.set_state(AnswerToState.message)
    await state.set_data({'user_id': user_id})
    
    await callback_query.message.answer(
        text='Відправте повідомлення для користувача⤵️',
        reply_markup=abort_send_ansver()
    )


@router.callback_query(F.data=='abort-reply-to')
async def abort_send_answer_to_user(
    callback_query: CallbackQuery, state: FSMContext) -> None:
    await callback_query.message.delete()
    current_state = await state.get_state()
        
    if current_state is not None:
        await state.clear()
        # await callback_query.message.answer(text='Відмінено 🫡')


@router.message(IsAdminFilter(), AnswerToState.message)
async def send_answer_to_user(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']
    await state.clear()
    
    
    await bot.copy_message(chat_id=user_id,
                           from_chat_id=message.chat.id,
                           message_id=message.message_id,
                           caption=message.caption,
                           caption_entities=message.caption_entities)


@router.message(IsAdminFilter())
async def message_without_state(message: Message) -> None:
    await message.answer(text='❗️Для того щоб відправити комусь повідомлення натисніть "Відповісти" під повідомленням користувача❗️')


    # if user_id!=admin_id:
    #     return message.answer(text=i18n.messages.choose_language(),
    #                       reply_markup=choose_lang_on_start_ikb())
    # else:
    #     return message.answer(text=i18n.messages.start_admin(name=user.name))
