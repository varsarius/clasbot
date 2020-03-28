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

@bot.command(pass_context=False)
@commands.has_role("Учитель")
async def openbio(ctx):
    print(Role("Учитель"))

async def time_check():
    while True:
        timeq = 1
        now = time.localtime(time.time())
        h = now.tm_hour + 2
        m = now.tm_min
        channel = bot.get_channel(691342588372058273)
        i = 8
        while i <= 13: # 8 - час + 5 - это кол-во уроков в день = 11
            if ((h == i == 8) and (m == 45 or m == 50 or m == 55)):
                await channel.send(f"До начала урока {60-m} минут")
                timeq = 90 #чтобы не приходило 60 сообщений
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
            i = i + 1
        await asyncio.sleep(timeq)
bot.loop.create_task(time_check())
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
