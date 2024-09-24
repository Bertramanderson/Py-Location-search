import sys
import threading
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
import asyncio
import pyautogui
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, JoinEvent
import win32api, win32con
import time
from gtts import gTTS
import os

client = TikTokLiveClient(unique_id="Tiktokname")  # tiktok name oder so

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

async def on_join(event: JoinEvent):
    mytext = f'Welcome {event.user.nickname}'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("sss.mp3")
    os.system('start sss.mp3')


async def on_comment(event: CommentEvent) -> None:
    global lines
    time.sleep (5)
    click(1407,244)
    pyautogui.typewrite(f"{event.comment}")
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    mytext = f'Searching {event.comment}'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system('start welcome.mp3')

client.add_listener(CommentEvent, on_comment)

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    myconct = f'Connected'
    language = 'en'
    myobj = gTTS(text=myconct, lang=language, slow=False)
    myobj.save("conected.mp3")
    os.system('start conected.mp3')
    await asyncio.sleep(5)
    click(1407,244)

client.add_listener(ConnectEvent, on_connect)

def run_client():
    client.run()

app = QtWidgets.QApplication(sys.argv)
w = QWebEngineView()
w.resize(1000, 900)
w.load(QtCore.QUrl('http://localhost:5173'))
w.setWindowFlags(w.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
w.show()

threading.Thread(target=run_client, daemon=True).start()
app.exec_()

print("Hello, world!")