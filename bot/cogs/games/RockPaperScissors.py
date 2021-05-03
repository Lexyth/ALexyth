from discord.ext import commands
from discord.ext.commands import Bot, Cog, command
import random

import database as db

class RockPaperScissors(Cog):
  
  
  choices = ['scissors', 'paper', 'rock']
  
  
  def __init__(self, bot : Bot):
    self.bot = bot
  
  
  @commands.command(name = 'RPSplay')
  async def play(self, ctx, choice) -> None:
    user_idx = 0
    choice = choice.lower()
    if isinstance(choice, str):
      if choice not in self.choices:
        await ctx.send(f"Please choose one of the following:\n{chr(10).join([f'{i+1}: {self.choices[i].capitalize()}' for i in range(len(self.choices))])}")
        return
      user_idx = self.choices.index(choice)
    elif isinstance(choice, int):
      if choice > 0 and choice <= len(self.choices):
        user = choice-1
      else:
        await ctx.send(f"Please choose one of the following:\n{chr(10).join([f'{i+1}: {self.choices[i].capitalize()}' for i in range(len(self.choices))])}")
    enemy_idx = random.randint(0,len(self.choices));
    
    user_choice = self.choices[user_idx].capitalize()
    enemy_choice = self.choices[enemy_idx].capitalize()
    
    if self.choices[user_idx] == self.choices[enemy_idx-1]:
      await ctx.send(f"{ctx.author.name} chose {user_choice}\nALexyth chose {enemy_choice}\n\n{user_choice} beats {enemy_choice}\nCongratulations! {ctx.author.name} won!")
      await self.record(ctx)
    elif self.choices[enemy_idx] == self.choices[user_idx-1]:
      await ctx.send(f"{ctx.author.name} chose {user_choice}\nALexyth chose {enemy_choice}\n\n{enemy_choice} beats {user_choice}\nALexyth won!")
    else :
      await ctx.send(f"{ctx.author.name} chose {user_choice}\nALexyth chose {enemy_choice}\n\nTie on {user_choice}")
  
  
  @play.error
  async def play_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Please choose one of the following:\n{chr(10).join([f'{i+1}: {self.choices[i].capitalize()}' for i in range(len(self.choices))])}")
  
  
  async def record(self, ctx):
    await db.execute("INSERT INTO LeaderboardRockPaperScissors (id, username, score, time) VALUES ($1, $2, $3, CURRENT_TIMESTAMP) ON CONFLICT (id) DO UPDATE SET score = LeaderboardRockPaperScissors.score+EXCLUDED.score;",ctx.author.id, ctx.author.name, 1)
  
  
  @commands.command(name = 'RPSleaderboard', aliases = ['RPSlb', 'RPSrank'])
  async def leaderboard(self, ctx):
    records = await db.fetch("SELECT * FROM LeaderboardRockPaperScissors;")
    lb = ""
    for record in records:
      lb+=f"Name: {record['username']} Score: {record['score']} Time: {record['time']}\n"
    await ctx.send(lb)


def setup(bot: Bot) -> None:
  bot.add_cog(RockPaperScissors(bot))