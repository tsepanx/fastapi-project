import requests
import random

from api import POST_ENDPOINT, POSTModel

hostname = "0.0.0.0"
port = 8001

base_domain = f'http://{hostname}:{port}'


def test_ping():
    url = base_domain + '/api/ping'

    r = requests.get(url).json()

    assert r == 'Ok'


def test_get_set():
    post_url = base_domain + POST_ENDPOINT
    print(post_url)

    url = str(random.randint(100, 1000))
    domain = 'me.xyz'

    data = POSTModel.construct(destination=url, domain=domain).json()

    j = requests.post(post_url, data).json()

    get_url = post_url + '/' + j['id']

    r = requests.get(get_url).json()

    print(j, r, sep='\n')

    assert r['destination'] == url
