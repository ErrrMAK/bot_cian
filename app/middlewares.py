from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable

class TestMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, 
                       data: Dict[str, Any]) -> Any:
        return await super().__call__(handler, event, data)