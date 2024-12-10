import time
import json
from discord import Bot
from discord import ApplicationContext
import discord
import commands as cmd
import dotenv
import os
from bot_announcements import announce_current
import asyncio


async def update_config(config):
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

global channel_name
global announcements_enabled
dotenv.load_dotenv()
discordkey = os.getenv('DISCORDKEY')
xmltvurl = os.getenv('XMLTVURL')
bot = Bot()
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    channel_name = config['CHANNEL_NAME']
    announcements_enabled = config['ANNOUNCEMENTS_ENABLED']
    admin_role_name = config['ADMIN_ROLE_NAME']


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await announce()


async def announce():
    while announcements_enabled == 'ENABLED':
        wait = await announce_current(bot)
        await asyncio.sleep(wait)


async def admin_check(ctx):
    for role in ctx.author.roles:
        if role.name == admin_role_name:
            return True
    else:
        return False


announcement_cmd = bot.create_group('announcements', 'Enable/Disable content announcements')


@announcement_cmd.command(description='Enables channel content announcements. Requires user role: ' + admin_role_name)
async def enable(ctx):
    if await admin_check(ctx) == True:
        global announcements_enabled
        announcements_enabled = 'ENABLED'
        config['ANNOUNCEMENTS_ENABLED'] = announcements_enabled
        await update_config(config)
        print('Announcements: ' + announcements_enabled)
        await ctx.respond('Announcements enabled.')
        await announce()
    else:
        await ctx.respond('This command is for admin users only.')

@announcement_cmd.command(description='Disables channel content announcements. Requires user role: ' + admin_role_name)
async def disable(ctx):
    if await admin_check(ctx) == True:
        global announcements_enabled
        announcements_enabled = 'DISABLED'
        config['ANNOUNCEMENTS_ENABLED'] = announcements_enabled
        await update_config(config)
        print('Announcements: ' + announcements_enabled)
        await ctx.respond('Announcements disabled.')
    else:
        await ctx.respond('This command is for admin users only.')

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


