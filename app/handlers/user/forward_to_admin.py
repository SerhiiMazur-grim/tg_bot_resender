from __future__ import annotations

from typing import Any, Final

from aiogram import F, Bot
from aiogram import Router
from aiogram.methods import TelegramMethod
from aiogram.types import Message

from aiogram_i18n import I18nContext

from services.database import DBUser
from app.filters.user_filter import IsUserFilter
from utils import to_input_media


router: Final[Router] = Router(name=__name__)


@router.message(IsUserFilter(), F.media_group_id)
async def forward_media_group_message(message: Message, bot: Bot, i18n: I18nContext,
                                      album: list = None) -> TelegramMethod[Any]:
    settings = i18n.data.get('settings')
    admin_id = settings.admin_id
    user_name = message.from_user.full_name
    
    media = to_input_media(album)
    await bot.send_media_group(admin_id, media)
    await bot.send_message(admin_id, f'Переслано від {user_name}')



@router.message(IsUserFilter())
async def forward_message_to_admin(message: Message, bot: Bot,
                                   i18n: I18nContext, user: DBUser) -> TelegramMethod[Any]:
    settings = i18n.data.get('settings')
    admin_id = settings.admin_id
    user_id = message.from_user.id

    return message.forward(admin_id)
    
    # if user_id!=admin_id:
    #     return message.answer(text=i18n.messages.choose_language(),
    #                       reply_markup=choose_lang_on_start_ikb())
    # else:
    #     return message.answer(text=i18n.messages.start_admin(name=user.name))


