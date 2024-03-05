from __future__ import annotations

from typing import Any, Final

from aiogram import Router, F
from aiogram.methods import TelegramMethod
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram_i18n import I18nContext

from services.database import DBUser, Repository
from app.keyboards.inline_kb import choose_lang_ikb


router: Final[Router] = Router(name=__name__)


@router.message(Command('language'))
async def init_change_lang(message: Message, i18n: I18nContext) -> TelegramMethod[Any]:
    return message.answer(text=i18n.messages.choose_language(),
                          reply_markup=choose_lang_ikb())


@router.callback_query(F.data.startswith('language'))
async def change_lang(callback_query: CallbackQuery, i18n: I18nContext,
                      user: DBUser, repository: Repository) -> TelegramMethod[Any]:
    await callback_query.message.delete()
    language: str = callback_query.data.split('_')[-1]
    await i18n.manager.set_locale(language, user, repository)
    return callback_query.message.answer(text=i18n.core.get('messages-language_is_set', language))


@router.callback_query(F.data.startswith('start-language'))
async def change_lang_on_start(callback_query: CallbackQuery, i18n: I18nContext,
                      user: DBUser, repository: Repository) -> TelegramMethod[Any]:
    await callback_query.message.delete()
    language: str = callback_query.data.split('_')[-1]
    await i18n.manager.set_locale(language, user, repository)
    return callback_query.message.answer(text=i18n.core.get('messages-start', language, name=user.name, chanel_name='CHANEL NAME'))
