import requests
import random

from api import ITEM_ENDPOINT, PING_ENDPOINT, GetModel

hostname = "0.0.0.0"
port = 8001

base_domain = f'http://{hostname}:{port}'


def test_ping():
    url = base_domain + PING_ENDPOINT

    r = requests.get(url).json()

    assert r == 'ok'


def test_get_set():
    post_url = base_domain + ITEM_ENDPOINT
    print(post_url)

    m_id = str(random.randint(100, 1000))
    m_name = m_id + '123'
    m_desc = m_id + 'desc'

    data = GetModel.construct(
        id=m_id,
        name=m_name,
        description=m_desc
    ).dict()

    print(data)
    print(type(data))

    j = requests.post(post_url, json=data)

    get_url = post_url + '/' + m_id

    r = requests.get(get_url).json()

    print(j, r, sep='\n')
