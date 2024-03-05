from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.methods import TelegramMethod
from aiogram.types import Message
from aiogram_i18n import I18nContext

from services.database import DBUser
from app.keyboards.inline_kb import choose_lang_on_start_ikb


router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: Message, i18n: I18nContext, user: DBUser) -> TelegramMethod[Any]:
    settings = i18n.data.get('settings')
    user_id = message.from_user.id
    admin_id = settings.admin_id
    
    if user_id!=admin_id:
        return message.answer(text=i18n.messages.choose_language(),
                          reply_markup=choose_lang_on_start_ikb())
    else:
        return message.answer(text=i18n.messages.start_admin(name=user.name))
