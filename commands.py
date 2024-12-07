import xmltvparse as xtv
import dotenv
import os


dotenv.load_dotenv()
xmltvurl = os.getenv('XMLTVURL')
mainchannel = os.getenv('MAINCHANNEL')


def help():
    return '/nowplaying - Shows what is currently playing \n/upnext - Shows what will play next'


def nowplaying():
    return xtv.getcurrent(xmltvurl, mainchannel)


def upnext():
    return xtv.getnext(xmltvurl, mainchannel)