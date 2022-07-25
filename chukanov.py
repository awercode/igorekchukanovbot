lang="python"
from vkbottle.bot import Bot, Message, rules
from vkbottle import GroupEventType, GroupTypes, Keyboard, KeyboardButtonColor, Text, VKAPIError, TemplateElement, template_gen
import random

photos_list = ["photo-203890312_457239017", "photo-203890312_457239018", "photo-203890312_457239019", "photo-203890312_457239020", "photo-203890312_457239021", "photo-203890312_457239022", "photo-203890312_457239023", "photo-203890312_457239024", "photo-203890312_457239025", "photo-203890312_457239026", "photo-203890312_457239027", "photo-203890312_457239028", "photo-203890312_457239050", "photo-203890312_457239051", "photo-203890312_457239054"]

messages_list = ["Ayuwoki hehee!", "ааа этш же чуканов афигеть круто", "что за хкйню я тут пишу", "IGREG", "может быть добавить старые сррьшея эеще", "NAGIEV", "Сделай скриншот\nОтправь боту (н ечуканову)", "Показать чуканова", "и ты мой последний предатель которого я не прощу", "говорит игорь ч.", "новый хит игоря чуканова", "между нами провоДА", "ахаха чуканов смешной", "ржака смеяка", "Good morning Elena ANATOLEVNA", "скотина"]

names_list = ["елена анатольевна", "карине егишевна", "дмитрий нагиев"]

bot = Bot(token="vk1.a._uzVQTrqQDnRtuhOPbWuPdx7H5aIJOioMltY0FKrGbK_hS7RTL0EKFtHQoE87Z3VjZ8tNGYKlW5rFy4oys7UqSqik21rbyjCsKiuytnYj1Sn0ywd_Q5HGwEg7joqiZH8_qYE6csEUcxscA_0Dna8ZEz3wqXg0_6ODUK91Kkl6G_FxzVU8M89555G3Xucwdk8")

bot.labeler.message_view.replace_mention = True

@bot.on.message(text="Показать чуканова")
async def pokazat_handler(message: Message):
    await message.answer(random.choice(messages_list), attachment=random.choice(photos_list))
    #await message.answer("тест, {}".format(users_info[0].first_name))

@bot.on.message(text=messages_list)
async def povtoryat_handler(message: Message):
    await message.answer("пизда " + random.choice(names_list) + " ты че за мной повторяешь")

@bot.on.message(text=["магазин", "нагиев"])
async def nagievhandler(message: Message):
    keyboardnagiev = Keyboard().add(Text("купить нагиева онлайн"), color=KeyboardButtonColor.POSITIVE)
    keyboarddivan = Keyboard().add(Text("купить диван"), color=KeyboardButtonColor.NEGATIVE)
    magazinkarusel = template_gen(
        TemplateElement(
            "Нагиев",
            "нагиев это",
            "-203890312_457239056",
            keyboardnagiev.get_json()
        ),
        TemplateElement(
            "Диван",
            "купить диван",
            "-203890312_457239057",
            keyboarddivan.get_json()
        )
    )
    
    await message.answer("уникальный магазин пятерочка чуканов бот платичег нагиев здесь вы можете купить всеДИВАН", template=magazinkarusel)

@bot.on.message(text="купить нагиева онлайн")
async def nagievhandler(message: Message):
    await message.answer("УРА ПОЗДРАВЛЯЮ ВЫ КУПИЛИ НАгИЕВА ОНЛАЙН ПОДЗДрАВЛЯЮ С ПОКУПКОЙ!!!!!!!11111")

@bot.on.message(text="купить диван")
async def divanhandler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("{} {} купила диван".format(users_info[0].first_name, users_info[0].last_name).lower())

#@bot.on.chat_message((rules.ChatActionRule("chat_invite_user"), rules.ChatActionRule("chat_invite_user_by_link")))
#async def user_joined(message: Message) -> None:
    #users_info = await bot.api.users.get(message.from_id)
#    await message.answer("ура новый чуканов пришел, {}".format(users_info[0].first_name))

@bot.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def group_join_handler(event: GroupTypes.GroupJoin):
    try:
        await bot.api.messages.send(
            peer_id=event.object.user_id, message="пизда чукано чуканов!", random_id=0
        )
    except VKAPIError[901]:
        pass

bot.run_forever()
