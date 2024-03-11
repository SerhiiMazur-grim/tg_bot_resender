from typing import Final

from aiogram import Router

from . import answer

router: Final[Router] = Router(name=__name__)
router.include_routers(answer.router)
