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
                content = {'title':programme[0].text}
                for child in programme:
                    if child.tag == 'episode-num' and child.get('system') == 'onscreen':
                        content['episode'] = child.text
                for child in programme:
                    if child.tag == 'desc' and child.get('lang') == 'en':
                        content['description'] = child.text
                if 'episode' not in content:
                    content['episode'] = ''
                return content


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
                content = {'title':programme[0].text}
                for child in programme:
                    if child.tag == 'episode-num' and child.get('system') == 'onscreen':
                        content['episode'] = child.text
                for child in programme:
                    if child.tag == 'desc' and child.get('lang') == 'en':
                        content['description'] = child.text
                if 'episode' not in content:
                    content['episode'] = ''
                return content