import os
import random
import discord
from discord.ext import commands, tasks
from discord import app_commands
from majorx_supabase import xp_increment, LIST_ID

# load_dotenv() is already called once in majorx_supabse which is initialized before this main file

# SECRETS
TOKEN = os.environ['TOKEN']

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

"""
@tasks.loop(seconds=125)
async def my_task():
  url = "https://discord.com/api/v9/channels/1000269442036543539/messages"
  header = {"Authorization": f"{majorx}"}
  payload = {"content" : "TESTING"}
  response = requests.post(url, headers=header, json=payload)
  msg_id = response.json()['id']
  await asyncio.sleep(4)
  url = f"https://discord.com/api/v9/channels/1000269442036543539/messages/{msg_id}"
  header = {"Authorization": f"{majorx}"}
  requests.delete(url, headers=header)
  print("SUCCESS")
"""

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
    #my_task.start()


# Give 1 XP when use ANY Argus Slash Command
@client.event
async def on_interaction(ctx: discord.Interaction):
  if ctx.type == discord.InteractionType.application_command and ctx.user.id in LIST_ID:
    await xp_increment(1, ctx.user.id)

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


# RUN BOT
client.run(TOKEN)

'''
keep_alive()
try:
    client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system('kill 1')
    system("python restarter.py")
'''