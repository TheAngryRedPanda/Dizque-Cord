import xmltvparse as xtv
import tvdb
import discord
import exceptions
import json
import datetime


with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    channel_id = config['ANNOUNCEMENTS_CHANNEL_ID']
    mainchannel = config['MAINCHANNEL']
    xmltvurl = config['XMLTVURL']


async def announce_current(bot):
    current_programme = xtv.getcurrent(xmltvurl, mainchannel)
    art_url = tvdb.get_art_url(current_programme['title'])

    embed = discord.Embed(
        title=current_programme['title']
    )
    embed.add_field(name=current_programme['episode'], value=current_programme['description'])
    embed.set_image(url=tvdb.get_art_url(current_programme['title']))
    content = 'Now playing:'
    await channel_send_message(content, channel_id, bot, embed)
    stop_time = datetime.datetime.strptime(current_programme['stop'], '%Y%m%d%H%M%S %z')
    now = datetime.datetime.now(datetime.UTC)
    deltatime = stop_time - now
    return(deltatime.seconds)


async def channel_send_message(content, channel_id, bot, embed=None):
    channel = bot.get_channel(1313559549554458706)
    await channel.send(content=content, embed=embed)