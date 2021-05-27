# main.py

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import csv
import time

# Use dotenv to conceal token.
load_dotenv()

# Other necessary variables 
TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX='ff!'
MEMBERS = []
CURRENT_FACT = None
NO_SOURCE = False
FACTS = []

# Command prefix
client = commands.Bot(command_prefix=COMMAND_PREFIX)

# Helpful loading prompt.
print("Starting bot...")

# Remove default help command to allow for help command.
client.remove_command('help')

# Error checking...
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try ' + COMMAND_PREFIX + 'help ({error})')

# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# Set custom status for bot.
async def custom_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a documentary!"))
                    

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    client.loop.create_task(custom_status())

# token
client.run(TOKEN, reconnect=True)