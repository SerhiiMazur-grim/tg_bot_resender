from aiogram.types import Message
from aiogram.filters import BaseFilter

from aiogram_i18n import I18nContext


class IsAdminFilter(BaseFilter):
    async def __call__(self, message: Message, i18n: I18nContext) -> bool:
        settings = i18n.data.get('settings')
        admin_id = settings.admin_id
        user_id = message.from_user.id
        
        return user_id == admin_id
