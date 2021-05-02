from discord.ext.commands import Bot, Cog, command
import random

import database as db

class RockPaperScissors(Cog):
  
  def __init__(self, bot : Bot):
    self.bot = bot

  @command(name = 'playRockPaperScissors', aliases = ['playRPS'])
  async def play(self, ctx, choice) -> None:
    choices = ['scissors', 'paper', 'rock']
    user = 0
    if isinstance(choice, str):
      if choice not in choices:
        await ctx.send("Invalid input")
        return
      user = choices.index(choice)
    elif isinstance(choice, int):
      user = choice
    enemy = random.randint(0,2);
    if user == enemy:
      await ctx.send(f"Tie on {choices[user]}")
    elif choices[user] == choices[enemy-1]:
      await ctx.send(f"{choices[user]} beats {choices[enemy]}: User wins!")
    else :
      await ctx.send(f"{choices[enemy]} beats {choices[user]}: Enemy wins!")
    await self.record(ctx)
  
  async def record(self, ctx):
    conn = await db.connect()
    await conn.execute("INSERT INTO LeaderboardRockPaperScissors (id, username, score, time) VALUES ($1, $2, $3, CURRENT_TIMESTAMP) ON CONFLICT (id) DO UPDATE SET score = LeaderboardRockPaperScissors.score+EXCLUDED.score;",ctx.author.id, ctx.author.name, 1)
    print("Inserted data")
    print("Result")
    print(await conn.fetch("SELECT * FROM LeaderboardRockPaperScissors;"))
    print("Closing connection")
    await conn.close()
    print("Connection closed")
  
  @command(aliases = ['lbRPS'])
  async def leaderboard(self, ctx):
    conn = await db.connect()
    records = await conn.fetch("SELECT * FROM LeaderboardRockPaperScissors;")
    lb = ""
    for record in records:
      lb+=f"Name: {record['username']} Score: {record['score']} Time: {record['time']}\n"
    await ctx.send(lb)

def setup(bot: Bot) -> None:
  bot.add_cog(RockPaperScissors(bot))