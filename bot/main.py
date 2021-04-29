import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
@commands.dm_only()
async def ping(ctx):
    await ctx.send("pong")

server.server()
bot.run(TOKEN)
