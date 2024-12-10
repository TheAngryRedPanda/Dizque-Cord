import xmltvparse as xtv
import tvdb
from discord import Embed
import exceptions
import json


with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    mainchannel = config['MAINCHANNEL']
    xmltvurl = config['XMLTVURL']
    admin_role_name = config['ADMIN_ROLE_NAME']


def help():
    embed = Embed(
        title='**Commands:**'
    )
    embed.add_field(name='**/nowplaying**', value='Displays the current streaming content', inline=False)
    embed.add_field(name='**/upnext**', value='Displays the next scheduled program', inline=False)
    embed.add_field(name='**/announcements enable**', value='Ensables channel content announcements. Requires user role: ' + admin_role_name, inline=False)
    embed.add_field(name='**/announcements disable**', value='Disables channel content announcements. Requires user role: ' + admin_role_name, inline=False)
    return embed


def nowplaying():
    current_programme = xtv.getcurrent(xmltvurl, mainchannel)
    art_url = tvdb.get_art_url(current_programme['title'])
    embed = Embed(
        title=current_programme['title']
    )
    embed.add_field(name=current_programme['episode'], value=current_programme['description'])
    embed.set_image(url=tvdb.get_art_url(current_programme['title']))
    return embed


def upnext():
    next_programme = xtv.getnext(xmltvurl, mainchannel)
    embed = Embed(
        title=next_programme['title']
    )
    embed.add_field(name=next_programme['episode'], value=next_programme['description'])
    embed.set_image(url=tvdb.get_art_url(next_programme['title']))
    return embed

