import discord 
from discord.exte import commands 
import asyncio
import os 

get_prefix = "f "


INTENTS = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=INTENTS,  activity= discord.Activity(type=discord.ActivityType.playing, name=f"Hi I am Fen!"), status=discord.Status.idle)



@client.event
async def on_ready():
	print("-- I am ready --")
 
 
 
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            raise e
        

for filename in os.listdir('./cogs./admin'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            raise e


if __name__ == "__main__":
    client.run("")

