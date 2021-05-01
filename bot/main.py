import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("TOKEN")

extensions = ['cogs.games.RockPaperScissors']

if __name__ == '__main__':
  for extension in extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abcdef"))
    cur.execute("SELECT * FROM test;")
    print(cur.fetchone())

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
