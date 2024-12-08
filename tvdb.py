import requests as rq
from urllib.parse import urljoin
import dotenv
import os
import exceptions


dotenv.load_dotenv()
apikey = os.getenv('TVDBKEY')
base_url = 'https://api4.thetvdb.com'


def auth_token():
    try:
        endpoint = '/v4/login'
        url = urljoin(base_url, endpoint)
        auth = rq.post(
            url,
            json={'apikey': apikey},
            headers={'accept': 'application/json', 'Content-Type': 'application/json'}
        )
        token = auth.json()['data']['token']
        return token
    except:
        raise exceptions.auth_error('Error authenticating with TVDB. Check your TVDB API key.')


def get_art_url(title):
    try:
        endpoint = '/v4/search'
        url = urljoin(base_url, endpoint)
        art_search = rq.get(
            url,
            headers={'accept': 'application/json', 'authorization':'Bearer ' + auth_token()},
            params={'query':title}
        )
        art_url = art_search.json()['data'][0]['image_url']
        return art_url
    except exceptions.auth_error as e:
        print(type(e) + e)
        return