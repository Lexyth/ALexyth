import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("TOKEN")

extensions = ['cogs.games.RockPaperScissors']

if __name__ == '__main__':
  for extension in extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command(name = "dm ping", aliases = ['dmping'])
@commands.dm_only()
async def dm_ping(ctx):
    await ctx.send("Private pong")

@bot.command(name = "guild ping", aliases = ['guildping'])
@commands.guild_only()
async def guild_ping(ctx):
    await ctx.send("Public pong")

server.server()
bot.run(TOKEN)
