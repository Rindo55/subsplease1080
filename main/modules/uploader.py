import asyncio
import os
import time
import aiohttp
import requests
import aiofiles


from main.modules.utils import format_time, get_duration, get_epnum, get_filesize, status_text, tags_generator, get_messages, b64_to_str, str_to_b64, send_media_and_reply, get_durationx

from main.modules.anilist import get_anime_name

from main.modules.anilist import get_anime_img

from main.modules.db import present_user, add_user
from main.modules.thumbnail import generate_thumbnail

from config import UPLOADS_ID

from pyrogram import Client, filters

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from main.modules.progress import progress_for_pyrogram

from os.path import isfile

import os

import time

from main import app, status

from pyrogram.errors import FloodWait

from main.inline import button1

async def upload_video(msg: Message,file,id,tit,name,ttl,sourcetext,untext,nyaasize):

    try:

        fuk = isfile(file)

        if fuk:

            r = msg

            c_time = time.time()

            duration = get_duration(file)
            durationx = get_durationx(file)
            size = get_filesize(file)

            ep_num = get_epnum(name)
            
            rest = tit

            thumbnail = await generate_thumbnail(id,file)

            filed = os.path.basename(file)
            filed = filed.replace("[1080p Web-DL]", "[720p x265] @animxt")
            fukpath = "downloads/" + filed
            caption = f"{filed}"
            caption = caption.replace("[720p x265] @animxt.mkv", "") 
            gcaption=f"**{caption}**" + "\n" +  f"__({tit})__" + "\n" + "━━━━━━━━━━━━━━━━━━━" + "\n" + "✓  `720p x265 10Bit`" + "\n" + f"✓  `English ~ Sub`" + "\n" + "#Encoded #HEVC"
            kayo_id = -1001642923224
            gay_id = 1159872623
            x = await app.send_document(

                kayo_id,

            document=file,

            caption=gcaption,

            file_name=filed,

            force_document=True,
                
            thumb=thumbnail
            )
            os.rename(file,fukpath)
            server = requests.get(url="https://api.gofile.io/getServer").json()["data"]["server"]
            uploadxz = requests.post(url=f"https://{server}.gofile.io/uploadFile", files={"upload_file": open(fukpath, 'rb')}).json()
            directlink = uploadxz["data"]["downloadPage"]    
            gotn_url = f"https://flashlink.in/api?api=aafa2d36a38398631679a74769a071b2154e08e7&url={directlink}&format=text"
            gofinal = requests.get(gotn_url)
            go_text = gofinal.text
            gourl = go_text
            da_url = "https://da.gd/"
            gofile_url = f"{da_url}shorten"
            goresponse = requests.get(gofile_url, params={"url": gourl})
            gofuk_text = goresponse.text.strip()
            file_er_id = str(x.message_id)
            share_link = f"https://telegram.me/somayukibot?start=animxt_{str_to_b64(file_er_id)}"
            enshare_link = f"https://flashlink.in/api?api=aafa2d36a38398631679a74769a071b2154e08e7&url={share_link}&format=text"
            fukshare = requests.get(enshare_link)
            tshare = fukshare.text
            cshare = tshare
            xshare_url = f"{da_url}shorten"
            tgshare = requests.get(xshare_url, params={"url": cshare})
            teleshare = tgshare.text.strip()    
            come_id = int(untext.message_id)
            come_link = f"t.me/c/{gay_id}/{come_id}?thread={come_id}"
            repl_markup=InlineKeyboardMarkup(
                    [
                        [
                             InlineKeyboardButton(
                                text="🐌TG FILE",
                                url=teleshare,
                            ),
                             InlineKeyboardButton(
                                  text="🚀GoFile",
                                  url=gofuk_text,
                            ),
                        ],
                    ],
                 )
            encodetext =  f"{sourcetext}" "\n" + f"**‣ File Size**: `{size}`" + "\n" + f"**‣ Duration**: {durationx}" + "\n" + f"**‣ Downloads**: [🔗Telegram File]({teleshare}) [🔗Gofile]({gofuk_text})"
            await asyncio.sleep(5)
            entext = await untext.edit(encodetext, reply_markup=repl_markup)
    except Exception:
            await app.send_message(kayo_id, text="Something Went Wrong!")
    try:

            await r.delete()

            os.remove(file)

            os.remove(thumbnail)

    except:

        pass

    return x.message_id
