from typing import Final

from aiogram import Router

from . import test

router: Final[Router] = Router(name=__name__)
router.include_routers(test.router)
