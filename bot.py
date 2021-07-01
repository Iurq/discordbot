import os
os.system("pip install discord")
from discord.ext import commands
from time import sleep

bot = commands.Bot(command_prefix='-')

potato = 0
money = 0
amount = 1
@bot.command()
async def farm(ctx):
    global potato
    global amount
    await ctx.send("You have requested a potato/s to grow. Come back in a minute to check on your potatos growth.")
    sleep(60)
    await ctx.send("Your potato has grown!")
    potato += amount

@bot.command()
async def potatosell(ctx):
  global money
  await ctx.send("Choose retailer to sell to :")
  await ctx.send("a - Alans Potato Shop (3 🥔 Required) (4 💵 per potato)")
  await ctx.send("b - Farm House Shop (10 🥔 Required) (11 💵 per potato)")
  await ctx.send("c - Fresh Foods Industry (20 🥔 Required) (21 💵 per potato)")
  await ctx.send("d - ASDA Supliers. (50 🥔 Required) (51 💵 per potato)")
  await ctx.send("e - Global Potato Market (100 🥔 Required) (101 💵 per potato)")
  @bot.command()
  async def a(ctx):
    if potato >= 3 :
      global money
      money += 4
      await ctx.send("You have sold 1 potato and gotten £4")
    else :
      await ctx.send("You do not meet the requirments for this command.")
  @bot.command()
  async def b(ctx):
    if potato >= 10 :
      global money
      money += 11
      await ctx.send("You have sold 1 potato and gotten £11")
    else :
      await ctx.send("You do not meet the requirments for this command.")
  @bot.command()
  async def c(ctx):
    if potato >= 20 :
      global money
      money += 21
      await ctx.send("You have sold 1 potato and gotten £21")
    else :
      await ctx.send("You do not meet the requirments for this command.")
  @bot.command()
  async def d(ctx):
    if potato >= 50 :
      global money
      money += 11
      await ctx.send("You have sold 1 potato and gotten £51")
    else :
      await ctx.send("You do not meet the requirments for this command.")
  @bot.command()
  async def e(ctx):
    if potato >= 100 :
      global money
      money += 101
      await ctx.send("You have sold 1 potato and gotten £101")
    else :
      await ctx.send("You do not meet the requirments for this command.")

@bot.command()
async def upgrade(ctx):
  if money >= 50 :
    await ctx.send("Would you like to spend 50 potato coins for a increase of 1 potato to be grown every minute? To confirm type -confirm")
    @bot.command()
    async def confirm(ctx):
      global amount
      global money
      amount += 1
      money -= 50
      await ctx.send("Confirmed! You now grow" + str(amount) + "per minute.")
  else :
    await ctx.send("You do not meet the requirments for this command.")
     
@bot.command()
async def balance(ctx):
  await ctx.send(str(potato) + "potatos and " + str(money) + "potato coins.")




bot.run('ODU5OTA5Mjk1ODYwMDg4ODYy.YNzi8A.ZhFu17LEjahkNSut1CiFlYAMDRY')
