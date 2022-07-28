#-*- coding: utf-8 -*-
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from aiohttp import Payload
from vkbottle.bot import Bot, Blueprint, Message, rules
from vkbottle import GroupEventType, GroupTypes, Keyboard, KeyboardButtonColor, Text, VKAPIError, TemplateElement, template_gen, ShowSnackbarEvent, Callback, PhotoMessageUploader, PhotoUploader
from vkbottle.dispatch.rules.base import CommandRule
import random
import asyncio
import requests
import logging
from typing import Tuple
from pathlib import Path

bp = Blueprint("Images generator")

logging.basicConfig(level=logging.INFO)

bp.labeler.vbml_ignore_case = True
bp.labeler.message_view.replace_mention = True

@bp.on.message(text="!genimage <textforimage>")
async def genimage(message: Message, textforimage: None):
    textforimage = textforimage
    if textforimage == "" or textforimage == None:
        await message.answer("вы забыли написать текст", attachment="photo-203890312_457239099")
    else:
        if message.attachments == []:
            await message.answer("Вы не прикрепили изображение!")
        else:
            photo_url = message.attachments[0].photo.sizes[-5].url
            imgorig = requests.get(photo_url)
            img_file = open('image.jpg', 'wb')
            img_file.write(imgorig.content)
            img_file.close() 
            
            img = Image.open('image.jpg')

            idraw = ImageDraw.Draw(img)

            W, H = img.size
            w, h = idraw.textsize(textforimage)

            #home = Path.home()
            #font_path = Path(home, "blueprints", "arial.ttf")

            headline = ImageFont.truetype("Arial", size = 30)
            idraw.text(((W-w)/2,(H-h)/2), textforimage, font=headline)

            img.save('imageandtext.jpg')

            photo_uploader = PhotoMessageUploader(message.ctx_api)
            photo_attachment = await photo_uploader.upload("imageandtext.jpg")
            await message.answer(attachment=photo_attachment)

@bp.on.message(text="!genimage")
async def genimagebeztexta(message: Message):
    await message.answer("вы забыли написать текст", attachment="photo-203890312_457239099")
