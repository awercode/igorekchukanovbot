#-*- coding: utf-8 -*-
from PIL import Image, ImageFilter
from aiohttp import Payload
from vkbottle.bot import Bot, Blueprint, Message, rules
from vkbottle import GroupEventType, GroupTypes, Keyboard, KeyboardButtonColor, Text, VKAPIError, TemplateElement, template_gen, ShowSnackbarEvent, Callback
from vkbottle.dispatch.rules.base import CommandRule
import random
import asyncio

bp = Blueprint("Images generator")

bp.labeler.vbml_ignore_case = True
bp.labeler.message_view.replace_mention = True

@bp.on.message(command=("genimage", ["!", "?", "/"]))
async def genimage(message: Message):
    await message.answer("генерирую изображение...")
    asyncio.sleep(3)
    await message.answer("не сделал")
