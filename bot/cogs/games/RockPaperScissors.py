from discord.ext.commands import Bot, Cog, command
import random

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

def setup(bot: Bot) -> None:
  bot.add_cog(RockPaperScissors(bot))