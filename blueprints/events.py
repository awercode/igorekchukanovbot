#-*- coding: utf-8 -*-
from aiohttp import Payload
from vkbottle.bot import Bot, Blueprint, Message, rules
from vkbottle import GroupEventType, GroupTypes, Keyboard, KeyboardButtonColor, Text, VKAPIError, TemplateElement, template_gen, ShowSnackbarEvent, Callback
from vkbottle.dispatch.rules.base import CommandRule
import random

bp = Blueprint("Events handler")

bp.labeler.vbml_ignore_case = True
bp.labeler.message_view.replace_mention = True

@bp.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def handle_message_event(event: GroupTypes.MessageEvent):
    print(event.object.payload)
    if event.object.payload == {'cmd': 'buynagiev'}:
        await bp.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=ShowSnackbarEvent(text="Вы успешно купили нагиева!").json(),
        )
        await bp.api.messages.send(
            peer_id=event.object.peer_id, message="УРА ПОЗДРАВЛЯЮ ВЫ КУПИЛИ НАгИЕВА ОНЛАЙН ПОДЗДрАВЛЯЮ С ПОКУПКОЙ!!!!!!!11111", random_id=0
        )
    elif event.object.payload == {'cmd': 'buydivan'}:
        await bp.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=ShowSnackbarEvent(text="Вы успешно купили диван!").json(),
        )
        users_info = await bp.api.users.get(event.object.user_id)
        await bp.api.messages.send(
            peer_id=event.object.peer_id, message="{} {} купила диван".format(users_info[0].first_name, users_info[0].last_name).lower(), random_id=0
        )
    elif event.object.payload == {'cmd': 'buytransportir'}:
        await bp.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=ShowSnackbarEvent(text="Вы успешно купили транспортир!").json(),
        )
        users_info = await bp.api.users.get(event.object.user_id)
        await bp.api.messages.send(
            peer_id=event.object.peer_id, message="{} {} купил транспортир".format(users_info[0].first_name, users_info[0].last_name).lower(), random_id=0
        )

@bp.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def group_join_handler(event: GroupTypes.GroupJoin):
    try:
        await bp.api.messages.send(
            peer_id=event.object.user_id, message="пизда чукано чуканов!", random_id=0
        )
    except VKAPIError[901]:
        pass