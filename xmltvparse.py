import xml.etree.ElementTree as ET
import requests
import datetime


def getcurrent(xmltvurl, mainchannel):
    xmltv = requests.get(xmltvurl)
    root = ET.fromstring(xmltv.content)
    currenttimestamp = datetime.datetime.now(datetime.UTC).strftime('%Y%m%d%H%M%S')
    for programme in root:
        if programme.tag == 'programme':
            if int(programme.get('start')[:15]) <= int(currenttimestamp) and int(programme.get('stop')[:15]) > int(
                    currenttimestamp) and programme.get('channel') == mainchannel:
                for child in programme:
                    if child.tag == 'episode-num' and child.get('system') == 'onscreen':
                        epnum = child.text
                return 'Now playing: ' + programme[0].text + ' - ' + epnum


def getnext(xmltvurl, mainchannel):
    xmltv = requests.get(xmltvurl)
    root = ET.fromstring(xmltv.content)
    currenttimestamp = datetime.datetime.now(datetime.UTC).strftime('%Y%m%d%H%M%S')
    for programme in root:
        if programme.tag == 'programme':
            if int(programme.get('start')[:15]) <= int(currenttimestamp) and int(programme.get('stop')[:15]) > int(
                    currenttimestamp) and programme.get('channel') == mainchannel:
                nextstarttime = int(programme.get('stop')[:15])
    for programme in root:
        if programme.tag == 'programme':
            if int(programme.get('start')[:15]) == nextstarttime and programme.get('channel') == mainchannel:
                for child in programme:
                    if child.tag == 'episode-num' and child.get('system') == 'onscreen':
                        epnum = child.text
                        return 'Up next: ' + programme[0].text + ' - ' + epnum