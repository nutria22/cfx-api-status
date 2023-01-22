import requests
import discord
from discord.ext import commands
import time

TOKEN = ''

bot = commands.Bot(command_prefix='!')

SERVER_ID = 'YOUR_SERVER_ID'

def get_fivem_status():
    try:
        r = requests.get('https://status.cfx.re/api/v2/status.json')
        data = r.json()
        status = data['status']['description']
        return status
    except:
        return "[Error]: Couldn't get request in enough time."

@bot.command()
async def fivem_status(ctx):
    status = get_fivem_status()
    await ctx.send(status)


while True:
    time.sleep(3600) # Espera 1 hora (3600 segundos)
    server = bot.get_guild(SERVER_ID)
    channel = server.default_channel
    status = get_fivem_status()
    await channel.send(status)

bot.run(TOKEN)
