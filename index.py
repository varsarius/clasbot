import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord.utils import get
from discord import message
from discord.guild import Guild
import os
client = discord.Client()
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

@bot.command()
async def test(ctx):
    channel = ctx.message.author.voice_channel
    await ctx.channel.send(channel)
    

alarm_time = '01:55'#24hrs
hour = 21
min = 32
channel_id = '691342588372058273'

async def time_check():
    while True:
        timeq = 1
        now = time.localtime()
        h = now.tm_hour
        m = now.tm_min
        messages = ('Test')
        channel = bot.get_channel(691342588372058273)
        if (h == 8 and m == 45):
            await channel.send("До начала урока 15 минут")
            timeq = 90
        elif (h == 8 and m == 50):
            await channel.send("До начала урока 10 минут")
        elif (h == 8 and m == 55):
            await channel.send("До начала урока 5 минут")
        elif (h == 9 and m == 0):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок начался")
        elif (h == 9 and m = 45):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок закончился")
        elif (h == 10 and m == 0):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок начался")
        elif (h == 10 and m = 45):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок закончился")
        elif (h == 11 and m == 0):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок начался")
        elif (h == 11 and m = 45):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок закончился")
        elif (h == 12 and m == 0):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок начался")
        elif (h == 12 and m = 45):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок закончился")
        elif (h == 12 and m == 0):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок начался")
        elif (h == 12 and m = 45):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок закончился")
        elif (h == 13 and m == 0):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок начался")
        elif (h == 13 and m = 45):
            await channel.send("Дзинь-Дзинь-Дзинь***Урок закончился")
        else:
           timeq = 1
        await asyncio.sleep(timeq)

bot.loop.create_task(time_check())

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
