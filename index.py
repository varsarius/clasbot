from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord.utils import get
from discord import message
from discord.guild import Guild
import os
import datetime
import time
import sqlite3
import requests
from bs4 import BeautifulSoup as bs
from discord.utils import get
bot = commands.Bot(command_prefix='/')

@bot.command(pass_context=True) #разрешаем передавать агрументы
async def echo(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент

@bot.event
async def on_member_join(member):
    channel = client.get_channel(690973529985777754)
    role = discord.utils.get(member.guild.roles, id=690966191581429912)
    await member.add_roles(role)

@bot.command()
@commands.has_any_role("Учитель", "Admin", "lowAdmin")
async def operm(ctx):
    for role in ctx.guild.roles:
        if role.name == "Ученик":
            await ctx.channel.set_permissions(role, send_messages=True)
            await ctx.channel.send("Ученикам теперь разрешено отправлять сообщения на этом канале")

@bot.command()
@commands.has_any_role("Учитель", "Admin", "lowAdmin")
async def cperm(ctx):
    for role in ctx.guild.roles:
        if role.name == "Ученик":
            await ctx.channel.set_permissions(role, send_messages=False)
            await ctx.channel.send("Ученикам теперь запрещено отправлять сообщения на этом канале")

# vars
raspisanie = {
    "monday": {
        "start": 9,
        "lessons": ["fizics","lromana","math","rus"]
    },
}

async def time_check():
    while True:
        timeq = 1
        now = time.localtime(time.time())
        channel = bot.get_channel(691342588372058273)
        h = now.tm_hour + 3
        m = now.tm_min
        w = now.tm_wday
        if (w == 0): #понедельник
            l = 8 # когда начинаются уроки - 1
            j = 4 # сколько всего уроков
        elif (w == 1): # вторник  ... и т.д
            l = 8
            j = 5
        elif (w == 2):
            i = 9
            j = 2
        elif (w == 3):
            i = 8
            j = 4
        elif (w == 4):
            i = 8
            j = 5
        elif (w == 5 or w == 6):
            i = 0
            j = 0

        if (i!=0 and j!=0):  # час, в котором начинаются оповещения - 2, потому, что Лондонское время(уроки в 9 - 2, (GMT+2) -1, чтобы предупредить об уроках(9-2-1=6))( а так же счётчик и просто вспомогательная перемнная)
            while i <= l+j: # 8 - час + 5 - это кол-во уроков в день = 11
                if ((h == i == l) and (m == 45 or m == 50 or m == 55)):
                    await channel.send(f"До начала урока {60-m} минут")
                    timeq = 90 #чтобы не приходило 60 сообщений
            # --------это часть с постоянными уроками-----------
                elif( h == i):
                    if(m == 0):
                        await channel.send("Дзинь-Дзинь-Дзинь***Урок начался")
                        timeq = 90 #чтобы не приходило 60 сообщений
                    elif(m == 45):
                        await channel.send("Дзинь-Дзинь-Дзинь***Урок закончился")
                        timeq = 90 #чтобы не приходило 60 сообщений
                    elif(m == 50 or m == 55):
                        await channel.send(f"До начала урока {60-m} минут")
                        timeq = 90 #чтобы не приходило 60 сообщений
                    else:
                        timeq = 1
                # --------это завершение проверки звонков-----------
                i = i + 1
            await asyncio.sleep(timeq)
bot.loop.create_task(time_check())
#**************************************************************************
@bot.command()
async def weather(ctx, *, name):

    def prognoz(href):
        r = requests.Session()
        res = r.get(href)
        ans = bs(res.content, 'html.parser')
        weather = ans.findChildren('body')[0]
        Weather = weather.find('div', class_ = 'det_pog')
        return Weather.find('p').get_text()
        r.close()


    s = requests.Session()
    res = s.get('https://goodmeteo.ru/poisk/?s=' + name)
    s.close()

    try:
        await ctx.send('**Расчитываем прогноз на сегодня...**')
        ans_bs = bs(res.content, 'html.parser')
        Choose = ans_bs.find_all('div', class_ = 'search_line')[0]
        search_name = Choose.find_all('a', target="_blank")[0].get_text().replace(' ', '')
        search_href = 'https://goodmeteo.ru' + Choose.find_all('a', target="_blank")[0]['href']
        await ctx.send(prognoz(search_href))
    except IndexError:
        await ctx.send('**Ничего не найдено, попробуйте изменить поиск**')
@bot.command()
async def search_video(ctx, name):

    await ctx.send('**Ищем видосик...**')
    s = requests.Session()
    res = s.get('https://www.youtube.com/results?search_query=' + name + '&pbj=1').content
    s.close()
    ans_bs = bs(res, 'html.parser')

    Videos = ans_bs.findChildren('body')[0]
    VIDEOS = Videos.find_all('div', class_ = 'yt-lockup-content')[0]
    ViDeos = VIDEOS.select('a[class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link"]')[0]['href']

    await ctx.send('https://youtube.com' + ViDeos)
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
