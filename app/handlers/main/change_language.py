from __future__ import annotations

from typing import Any, Final

from aiogram import Router, F
from aiogram.methods import TelegramMethod
from aiogram.types import Message
from aiogram_i18n import I18nContext

from services.database import DBUser, Repository


router: Final[Router] = Router(name=__name__)


@router.message(F.text=='en')
async def change_lang(message: Message, i18n: I18nContext,
                      user: DBUser, repository: Repository) -> TelegramMethod[Any]:
    await i18n.manager.set_locale('en', user, repository)
    return message.answer(text='Local set to en')

@router.message(F.text=='uk')
async def change_lang(message: Message, i18n: I18nContext,
                      user: DBUser, repository: Repository) -> TelegramMethod[Any]:
    await i18n.manager.set_locale('uk', user, repository)
    return message.answer(text='Local set to uk')

@router.message(F.text=='ru')
async def change_lang(message: Message, i18n: I18nContext,
                      user: DBUser, repository: Repository) -> TelegramMethod[Any]:
    await i18n.manager.set_locale('ru', user, repository)
    return message.answer(text='Local set to ru')