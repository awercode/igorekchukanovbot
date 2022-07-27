#-*- coding: utf-8 -*-
from aiohttp import Payload
from vkbottle.bot import Bot, Blueprint, Message, rules
from vkbottle import GroupEventType, GroupTypes, Keyboard, KeyboardButtonColor, Text, VKAPIError, TemplateElement, template_gen, ShowSnackbarEvent, Callback
from vkbottle.dispatch.rules.base import CommandRule
import random

bp = Blueprint("Shop")

bp.labeler.vbml_ignore_case = True
bp.labeler.message_view.replace_mention = True

@bp.on.message(text=["магазин", "нагиев"])
async def nagievhandler(message: Message):
    keyboardnagiev = (
        Keyboard(one_time=False)
        .add(Callback("Купить", payload={"cmd": "buynagiev"}))
        .add(Callback("Цена: 1,28 ₽", payload={"cmd": "buynagiev"}))
        .get_json()
    )
    keyboarddivan = (
        Keyboard(one_time=False)
        .add(Callback("Купить", payload={"cmd": "buydivan"}))
        .add(Callback("Цена: 90 800,00 ₽", payload={"cmd": "buydivan"}))
        .get_json()
    )
    keyboartransportir = (
        Keyboard(one_time=False)
        .add(Callback("Купить", payload={"cmd": "buytransportir"}))
        .add(Callback("Цена: 67,00 ₽", payload={"cmd": "buytransportir"}))
        .get_json()
    )
    magazinkarusel = template_gen(
        TemplateElement(
            "Дмитрий Нагиев",
            "дядя нагиев",
            "-203890312_457239056",
            keyboardnagiev
        ),
        TemplateElement(
            "Диван",
            "купить диван",
            "-203890312_457239057",
            keyboarddivan
        ),
        TemplateElement(
            "Транспортир",
            "DZHAGAZPANYAN",
            "-203890312_457239085",
            keyboartransportir
        )
    )
    
    await message.answer("уникальный магазин пятерочка чуканов бот платичег нагиев здесь вы можете купить всеДИВАН", template=magazinkarusel)