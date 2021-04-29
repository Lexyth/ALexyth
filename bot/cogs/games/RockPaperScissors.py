from discord.ext.commands import Bot, Cog, Command
import random

class RockPaperScissors(Cog):
  
  choices = ['scissors', 'paper', 'rock']
  
  def __init__(self, bot : Bot):
    self.bot = bot

  @command(name = 'playRockPaperScissors', aliases = ['playRPS'])
  async def play(self, ctx, choice) -> None:
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
      print(f"Tie on {choices[user]}\n")
    elif choices[user] == choices[enemy-1]:
      print(f"{choices[user]} beats {choices[enemy]}: User wins!\n")
    else :
      print(f"{choices[enemy]} beats {choices[user]}: Enemy wins!\n")

def setup(bot: Bot) -> None:
  bot.add_cog(RockPaperScissors(bot))