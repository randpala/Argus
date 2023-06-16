import discord
import os
from os import system
import random
from keep_alive import keep_alive
import requests
from discord.ext import commands
from discord import app_commands

my_secret = os.environ['TOKEN']

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@client.event
async def on_ready():
    print('{0.user} is now in your server!'.format(client))
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="over Nobles server"))
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


#@client.event
#async def on_message(message):
    #if message.content.startswith('!sendit9'):
      #Lord_Aran = 876129174648152097
      #channel = client.get_channel(999502780224000100)
      #await channel.send("If there are any rules that you disagree with or have questions about, we encourage you to reach out to <@{}>.".format(Lord_Aran))



@client.tree.command(name="proposition")
async def proposition(ctx: discord.Interaction):
    """Generate a random proposition"""
    with open("debate_db.txt", "r") as file:
      debates = file.readlines()
    debate = random.choice(debates)
    embed = discord.Embed(title="Random Proposition",
                          description=debate,
                          color=0xeb6a5c)
    await ctx.response.send_message(embed=embed)



keep_alive()
try:
    client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system('kill 1')
    system("python restarter.py")
