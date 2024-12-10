import time
import json
from discord import Bot
from discord import ApplicationContext
import discord
import commands as cmd
import dotenv
import os
from bot_announcements import announce_current


dotenv.load_dotenv()
discordkey = os.getenv('DISCORDKEY')
xmltvurl = os.getenv('XMLTVURL')
bot = Bot()
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    channel_name = config['CHANNEL_NAME']


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


async def announce():
    time.sleep(announce_current(bot))


@bot.slash_command(name="nowplaying", description="Now Playing on " + channel_name)
async def nowplaying(ctx: ApplicationContext):
    await ctx.respond('Currently playing is:', embed=cmd.nowplaying())



@bot.slash_command(name="upnext", description="Up Next on " + channel_name)
async def upnext(ctx: ApplicationContext):
    await ctx.respond('Up next is :', embed=cmd.upnext())


@bot.slash_command(name="help", description="Commands")
async def help(ctx: ApplicationContext):
    await ctx.respond(embed=cmd.help())

try:
    bot.run(discordkey)
except discord.errors.LoginFailure as e:
    print('Unable to authenticate discord key.')


