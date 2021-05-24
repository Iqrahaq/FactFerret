# Bot.py

import discord
from discord.ext import commands
from discord.utils import get
import os
import mysql.connector
import random
import json
import asyncio

COMMAND_PREFIX='ff!'


class Bot(commands.Cog):
    """ a class filled with all commands related to the bot. """

    def __init__(self, client):
        self.client = client  

    # First command to be run before all other commands (to help with setting up DB and Role).
    @commands.command()
    async def botsetup(self, ctx):
        # Set timezone.
        await ctx.send('What\'s the timezone?')
        # Set time for bot to send daily facts

        # Set channel to send facts to.

        # Choose category of facts.

        
    # Searches for books (generic search that is similar to setbook).
    @commands.command()
    async def forcefact(self, ctx):
        # Force a fact to be sent to the fact's channel.
        await ctx.send('To be coded.')
        
    # Answers with a random quote - using quotes.json.
    @commands.command()
    async def quote(self, ctx):
        with open('./info/quotes.json', 'r') as quotes_file:
            quotes = json.load(quotes_file)
            responses = quotes
            random.seed(a=None)
            response = random.choice(responses)
        await ctx.send(response["text"] + ' - ' + response["author"])

        
    #######   TROUBLESHOOTING AND INFORMATION ########


    # Returns information about bot.
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(colour=discord.Colour.green())
        embed = discord.Embed(title='FactFerret (Bot)', url='https://github.com/Iqrahaq/FactFerret',
                                description='A bot to help provide facts every day.', color=0x5ae000)
        embed.set_author(name='Iqra Haq', url='https://www.iqrahaq.com')
        embed.set_thumbnail(url='https://github.com/Iqrahaq/FactFerret/raw/master/img/factferret-01.png')
        embed.add_field(name='How to use?', value='Use the "' + COMMAND_PREFIX + 'help" command!', inline=False)
        embed.add_field(name='Am I new?', value='Use the "' + COMMAND_PREFIX + 'botsetup" command!', inline=False)
        await ctx.send(embed=embed)
        


    # Ping to answer with the ms latency, helpful for troubleshooting.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms ')



    # Help list and details of commands...
    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(name='Help - List of commands available: ')
        embed.add_field(name=COMMAND_PREFIX+'ping', value='Returns my response time in milliseconds.', inline=False)
        embed.add_field(name=COMMAND_PREFIX+'info', value='Returns information about me.', inline=False)
        embed.add_field(name=COMMAND_PREFIX+'botsetup', value='If I\'m new, use this command to go through the necessary steps to set me up for your server.', inline=False)
        embed.add_field(name=COMMAND_PREFIX+'forcefact', value='Force a fact to be sent to the setup fact\'s channel.', inline=False)
        embed.add_field(name=COMMAND_PREFIX+'quote', value='Returns an inspirational quote.', inline=False)
        embed.set_thumbnail(url='https://raw.githubusercontent.com/Iqrahaq/FactFerret/master/img/factferret-01.png')
        embed.set_footer(text="© Iqra Haq")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Bot(client))


