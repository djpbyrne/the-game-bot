# Code based on sample from: https://realpython.com/how-to-make-a-discord-bot-python/

import os
import discord 
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

bot = commands.Bot(command_prefix='/')

@bot.command(name='lost')
async def lose_the_game(ctx):
    user = ctx.author
    await ctx.message.delete()
    await ctx.send(f'@here, {user.mention} lost the game')

bot.run(TOKEN)