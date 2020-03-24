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
@commands.has_any_role("Учитель", "Admin")
async def operm(ctx):
    for role in ctx.guild.roles:
        if role.name == "Ученик":
            await ctx.channel.set_permissions(role, send_messages=True)
            await ctx.channel.send("Ученикам теперь разрешено отправлять сообщения на этом канале")

@bot.command()
@commands.has_any_role("Учитель", "Admin")
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
    await ctx.channel.send(client.voice_clients.user)

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
