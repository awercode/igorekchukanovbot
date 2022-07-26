from aiohttp import Payload
from vkbottle.bot import Bot, Message, rules
from vkbottle import GroupEventType, GroupTypes, Keyboard, KeyboardButtonColor, Text, VKAPIError, TemplateElement, template_gen, ShowSnackbarEvent, Callback
from vkbottle.dispatch.rules.base import CommandRule
import random

photos_list = [
    "photo-203890312_457239017", "photo-203890312_457239018", "photo-203890312_457239019", "photo-203890312_457239020",
    "photo-203890312_457239021", "photo-203890312_457239022", "photo-203890312_457239023", "photo-203890312_457239024",
    "photo-203890312_457239025", "photo-203890312_457239026", "photo-203890312_457239027", "photo-203890312_457239028",
    "photo-203890312_457239050", "photo-203890312_457239051", "photo-203890312_457239054", "photo-203890312_457239058",
    "photo-203890312_457239059", "photo-203890312_457239068", "photo-203890312_457239069", "photo-203890312_457239070",
    "photo-203890312_457239071", "photo-203890312_457239072", "photo-203890312_457239073", "photo-203890312_457239074",
    "photo-203890312_457239075", "photo-203890312_457239076", "photo-203890312_457239077", "photo-203890312_457239078",
    "photo-203890312_457239079", "photo-203890312_457239080", "photo-203890312_457239081", "photo-203890312_457239082",
    "photo-203890312_457239083", "photo-203890312_457239084", "video-203890312_456239017", "video-203890312_456239021"
]

messages_list = [
    "Ayuwoki hehee!", "ааа этш же чуканов афигеть круто", "что за хкйню я тут пишу", "IGREG",
    "может быть добавить старые сррьшея эеще", "NAGIEV", "Сделай скриншот\nОтправь боту (н ечуканову)",
    "Показать чуканова", "и ты мой последний предатель которого я не прощу", "говорит игорь ч.",
    "новый хит игоря чуканова", "между нами провоДА", "ахаха чуканов смешной", "ржака смеяка",
    "Good morning Elena ANATOLEVNA", "скотина", "кто оскорбляет анатольевну тот скотина",
    "ANATOLEVNA SMESHNAYA"]

names_list = ["елена анатольевна", "карине егишевна", "дмитрий нагиев"]

bot = Bot(token="vk1.a._uzVQTrqQDnRtuhOPbWuPdx7H5aIJOioMltY0FKrGbK_hS7RTL0EKFtHQoE87Z3VjZ8tNGYKlW5rFy4oys7UqSqik21rbyjCsKiuytnYj1Sn0ywd_Q5HGwEg7joqiZH8_qYE6csEUcxscA_0Dna8ZEz3wqXg0_6ODUK91Kkl6G_FxzVU8M89555G3Xucwdk8")
bot.labeler.vbml_ignore_case = True

bot.labeler.message_view.replace_mention = True

@bot.on.message(text="Меню")
async def menu_handler(message: Message):
    MenuKeyboard = (
        Keyboard(one_time=False, inline=False)
        .add(Text("Показать чуканова"), color=KeyboardButtonColor.NEGATIVE)
        .row()
        .add(Text("Магазин"), color=KeyboardButtonColor.PRIMARY)
        .add(Text("Помощь"), color=KeyboardButtonColor.SECONDARY)
        .get_json()
    )
    await message.answer("меню бота чуканов бот", attachment=random.choice(photos_list), keyboard=MenuKeyboard)

@bot.on.message(text="Помощь")
async def pomogimne(message: Message):
    await message.answer(
        "💡Команды бота:\n\
        🤰Показать чуканова – показывает чуканова\n\
        📌Меню – обновляет меню\n\
        ⚠️Стикер это важно – отправляет илью олю важную\n\
        💪Любой другой стикер – присылает его id (может быть полезно, но в данном случае скорее всего только мне)\n\
        🛒Магазин – открывает меню магазина, где можно купить нагиева, диван и остальное потом\n\
        😮скинь страшную фотку чуканова – скидывает страшную фотк учуканова"
    )

@bot.on.message(text="Показать чуканова")
async def pokazat_handler(message: Message):
    if message.peer_id == 2000000002:
        colvosoobsheniyspam = random.randint(0, 300)
        for i in range(colvosoobsheniyspam):
            await message.answer(random.choice(messages_list), attachment=random.choice(photos_list))
        await message.answer(f"💡Отправлено сообщений: {colvosoobsheniyspam}")
    else:
        await message.answer(random.choice(messages_list), attachment=random.choice(photos_list))
    print(message.peer_id)

@bot.on.message(attachment="sticker")
async def sticker_handler(message: Message):
    if message.attachments[0].sticker.sticker_id == 62951:
        await message.answer(attachment="photo-203890312_457239059")
    else:
        await message.answer(f"ℹ️ID стикера: {message.attachments[0].sticker.sticker_id}")

#@bot.on.message(sticker=62951)
#async def etovajno(message: Message):
    #await message.answer(attachment="photo-203890312_457239059")

@bot.on.message(text=messages_list)
async def povtoryat_handler(message: Message):
    await message.answer("пизда " + random.choice(names_list) + " ты че за мной повторяешь")

@bot.on.message(text=["магазин", "нагиев"])
async def nagievhandler(message: Message):
    #keyboardnagiev = Keyboard().add(Text("купить нагиева онлайн"), color=KeyboardButtonColor.POSITIVE)
    keyboardnagiev = (
        Keyboard(one_time=False)
        .add(Callback("Купить", payload={"cmd": "buynagiev"}))
        .get_json()
    )
    #keyboarddivan = Keyboard().add(Text("купить диван"), color=KeyboardButtonColor.NEGATIVE)
    keyboarddivan = (
        Keyboard(one_time=False)
        .add(Callback("Купить", payload={"cmd": "buydivan"}))
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
        )
    )
    
    await message.answer("уникальный магазин пятерочка чуканов бот платичег нагиев здесь вы можете купить всеДИВАН", template=magazinkarusel)

@bot.on.message(text="скинь страшную фотку чуканова")
async def strashnochukanov(message: Message):
    await message.answer(attachment="photo-203890312_457239076")

@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def handle_message_event(event: GroupTypes.MessageEvent):
    print(event.object.payload)
    if event.object.payload == {'cmd': 'buynagiev'}:
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=ShowSnackbarEvent(text="Вы успешно купили нагиева!").json(),
        )
        await bot.api.messages.send(
            peer_id=event.object.peer_id, message="УРА ПОЗДРАВЛЯЮ ВЫ КУПИЛИ НАгИЕВА ОНЛАЙН ПОДЗДрАВЛЯЮ С ПОКУПКОЙ!!!!!!!11111", random_id=0
        )
    elif event.object.payload == {'cmd': 'buydivan'}:
        await bot.api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=ShowSnackbarEvent(text="Вы успешно купили диван!").json(),
        )
        users_info = await bot.api.users.get(event.object.user_id)
        await bot.api.messages.send(
            peer_id=event.object.peer_id, message="{} {} купила диван".format(users_info[0].first_name, users_info[0].last_name).lower(), random_id=0
        )

@bot.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def group_join_handler(event: GroupTypes.GroupJoin):
    try:
        await bot.api.messages.send(
            peer_id=event.object.user_id, message="пизда чукано чуканов!", random_id=0
        )
    except VKAPIError[901]:
        pass

bot.run_forever()
