import xmltvparse as xtv
import tvdb
import discord
import exceptions
import json
import datetime
import time


with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    channel_id = int(config['ANNOUNCEMENTS_CHANNEL_ID'])
    mainchannel = config['MAINCHANNEL']
    xmltvurl = config['XMLTVURL']
    announcements_enabled = config['ANNOUNCEMENTS_ENABLED']


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
    deltatime = deltatime + datetime.timedelta(seconds=30)
    print('Announcing next program in: ' + str(deltatime))
    return(deltatime.seconds)


async def channel_send_message(content, channel_id, bot, embed=None):
    channel = bot.get_channel(channel_id)
    await channel.send(content=content, embed=embed)