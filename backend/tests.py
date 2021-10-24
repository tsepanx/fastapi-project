import requests
import random

from backend.api.endpoints import items
from backend.api.endpoints.items import GetModel
from backend.utils import ok_status

hostname = "0.0.0.0"
port = 8001

base_domain = f'http://{hostname}:{port}'


def test_ping():
    url = base_domain

    r = requests.get(url).json()

    assert r == ok_status


def test_get_set():
    post_url = base_domain + items.router.prefix
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

    j = requests.post(post_url, json=data).json()

    assert j == ok_status

    get_url = post_url + '/' + m_id

    r = requests.get(get_url).json()

    print(j, r, sep='\n')

    assert r['id'] == m_id
