from discord import Bot
from discord import ApplicationContext
import discord
import commands as cmd
import dotenv
import os
from bot_announcements import announce_current
import asyncio
import config


#initialization
global discordkey
dotenv.load_dotenv()
discordkey = os.getenv('DISCORDKEY')
bot = Bot()
announcement_cmd = bot.create_group('announcements', 'Enable/Disable content announcements')


async def announce():
    while True:
        if config.get_config_value('ANNOUNCEMENTS_ENABLED') == 'ENABLED':
            wait = await announce_current(bot)
            await asyncio.sleep(wait)
        else:
            await asyncio.sleep(60)

async def admin_check(ctx):
    for role in ctx.author.roles:
        if role.name == config.get_config_value('ADMIN_ROLE_NAME'):
            return True
    else:
        return False


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await announce()


@announcement_cmd.command(description='Enables channel content announcements. Requires user role: ' + config.get_config_value('ADMIN_ROLE_NAME'))
async def enable(ctx):
    if await admin_check(ctx) == True:
        #global announcements_enabled
        #config.get_config_value("") = 'ENABLED'
        conf = config.get_config_json()
        conf['ANNOUNCEMENTS_ENABLED'] = 'ENABLED'
        config.update_config(conf)
        print('Announcements: ' + conf['ANNOUNCEMENTS_ENABLED'])
        await ctx.respond('Announcements enabled.')
    else:
        await ctx.respond('This command is for admin users only.')


@announcement_cmd.command(description='Disables channel content announcements. Requires user role: ' + config.get_config_value('ADMIN_ROLE_NAME'))
async def disable(ctx):
    if await admin_check(ctx) == True:
        global announcements_enabled
        announcements_enabled = 'DISABLED'
        conf = config.get_config_json()
        conf['ANNOUNCEMENTS_ENABLED'] = announcements_enabled
        config.update_config(conf)
        print('Announcements: ' + announcements_enabled)
        await ctx.respond('Announcements disabled.')
    else:
        await ctx.respond('This command is for admin users only.')


@bot.slash_command(name="nowplaying", description="Now Playing on " + config.get_config_value('CHANNEL_NAME'))
async def nowplaying(ctx: ApplicationContext):
    await ctx.respond('Currently playing is:', embed=cmd.nowplaying())


@bot.slash_command(name="upnext", description="Up Next on " + config.get_config_value('CHANNEL_NAME'))
async def upnext(ctx: ApplicationContext):
    await ctx.respond('Up next is :', embed=cmd.upnext())


@bot.slash_command(name="help", description="Commands")
async def help(ctx: ApplicationContext):
    await ctx.respond(embed=cmd.help())


try:
    bot.run(discordkey)
except discord.errors.LoginFailure as e:
    print('Unable to authenticate discord key.')