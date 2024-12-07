from discord import Bot
from discord import ApplicationContext
import commands as cmd
import dotenv
import os


dotenv.load_dotenv()
discordToken = os.getenv('DISCORDTOKEN')
xmltvurl = os.getenv('XMLTVURL')
bot = Bot()
mainchannel = os.getenv('MAINCHANNEL')


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="nowplaying", description="Now Playing on Cartoon Network ReVamped")
async def nowplaying(ctx: ApplicationContext):
    await ctx.respond(cmd.nowplaying())


@bot.slash_command(name="upnext", description="Up Next on Cartoon Network ReVamped")
async def upnext(ctx: ApplicationContext):
    await ctx.respond(cmd.upnext())


@bot.slash_command(name="help", description="Commands")
async def help(ctx: ApplicationContext):
    await ctx.respond(cmd.help())


bot.run(discordToken)  # run the bot with the token
