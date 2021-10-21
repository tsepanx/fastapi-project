import requests, json
import random

from main import item_endpoint


def test_get_set():
    hostname = "0.0.0.0"
    port = 8001

    post_url = f'http://{hostname}:{port}' + item_endpoint

    url = str(random.randint(100, 1000))
    desc = url + 'desc'

    data = {
        'url': url,
        'description': desc
    }

    j = requests.post(post_url, json.dumps(data)).json()

    get_url = f'http://{hostname}:{port}{item_endpoint}?id={j["id"]}'

    r = requests.get(get_url).json()

    print(j, r, sep='\n')
    assert j == r
