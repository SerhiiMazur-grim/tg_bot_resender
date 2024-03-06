from typing import Final

from aiogram import Router

from . import forward_to_admin

router: Final[Router] = Router(name=__name__)
router.include_routers(forward_to_admin.router)
