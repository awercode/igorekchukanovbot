#-*- coding: utf-8 -*-
from vkbottle import Bot, load_blueprints_from_package
import os
from blueprints import bps
import logging

bot = Bot(token=os.environ['TOKEN'])

logging.basicConfig(level=logging.INFO)

bot.labeler.vbml_ignore_case = True
bot.labeler.message_view.replace_mention = True

for bp in bps:
    bp.load(bot)

bot.run_forever()