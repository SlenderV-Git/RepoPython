from aiogram.types import Message
from aiogram.filters import BaseFilter
from Utilities.db_controller import get_admin_list

class IsAdmin(BaseFilter):
    async def __call__(self, message) -> bool:
        return True if message.from_user.id in get_admin_list() else False
    
