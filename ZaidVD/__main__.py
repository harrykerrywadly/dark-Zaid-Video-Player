# ===========
# Zaid Is Running
# ===========

import logging
import time
import sys
import asyncio
import glob
import importlib
from pathlib import Path
from pyrogram import Client, idle
from config import Zaid 
from ZaidVD.videoplayer import app
from ZaidVD.videoplayer import call_py
from helpers.loggings import LOG
 
    
ZaidVD = Client(
    ":memory:",
    Zaid.API_ID,
    Zaid.API_HASH,
    bot_token=Zaid.BOT_TOKEN,
    plugins=dict(root="ZaidVD"),
)

StartTime = time.time()

loop = asyncio.get_event_loop()

_path = f"ZaidVD/*.py"
files = glob.glob(_path)

def load_plugins(plugin_name):
    path = Path(f"ZaidVD/{plugin_name}.py")
    name = "ZaidVD.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(load)
    sys.modules[f"ZaidVD." + plugin_name] = load
    print("Imported => " + plugin_name)

async def start():
    print('\n')
    print('------------------ Initalizing ZAID --------------------')
    if ZaidVD:
        await ZaidVD.start()
    await app.start()
    await call_py.start()
    print('------------------------ DONE --------------------------')
    print('------------------ Importing Modules -------------------')
    for name in files:
        with open(name) as a:
            path_ = Path(a.name)
            plugin_name = path_.stem
            load_plugins(plugin_name.replace(".py", ""))
    print('------------------- INITIATED ZAID ---------------------')
    print('     Logged in as User =>> {}'.format((await app.get_me()).first_name))
    if ZaidVD:
        print('     Logged in to Bots =>> {}'.format((await bot.get_me()).first_name))
    print('--------------------------------------------------------')
    await idle()
if __name__ == '__main__':
    is_bot = bool(Zaid.BOT_TOKEN)
    loop.run_until_complete(start())


# ZaidVD.start()
# print("[STATUS]:✅ »» BOT CLIENT STARTED ««")
# app.start()
# print("[STATUS]:✅ »» USERBOT CLIENT STARTED ««")
# call_py.start()
# print("[STATUS]:✅ »» PYTGCALLS CLIENT STARTED ««")
# idle()
# print("[STATUS]:❌ »» BOT STOPPED ««")
