from pprint import pprint

import requests
import secrets

from app import schemas
from app.api.endpoints import items
from app.core.config import settings
from app.schemas import Item
from app.utils import ok_status

hostname = settings.HTTP_HOST
port = settings.HTTP_PORT

base_domain = f'http://{hostname}:{port}'

post_url = base_domain + items.router.prefix


def test_ping():
    url = base_domain

    r = requests.get(url).json()

    assert r == ok_status


def test_get_set():
    m_title = '123_test'
    m_text = 'text_test'

    data = schemas.ItemCreate.construct(
        title=m_title,
        text=m_text
    ).dict()

    j = requests.post(post_url, json=data)

    pprint(j.json())
    pprint(data)
    assert schemas.ItemCreate(**j.json()) == schemas.ItemCreate(**data)
    assert j.status_code == 201

    item_id = j.json()['id']

    get_url = post_url + '/' + item_id

    r = requests.get(get_url).json()

    # print(j, r, sep='\n')

    assert r['id'] == item_id
    assert r['title'] == m_title
