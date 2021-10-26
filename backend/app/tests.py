import requests
import secrets

from app import schemas
from app.api.endpoints import items
from app.core.config import settings
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
    m_id = secrets.token_urlsafe(32)
    m_title = m_id + '123_test'
    m_text = m_id + 'text_test'

    data = schemas.ItemCreate.construct(
        id=m_id,
        title=m_title,
        text=m_text
    ).dict()

    print(data)
    print(type(data))

    j = requests.post(post_url, json=data)

    assert j.json() == data
    assert j.status_code == 201

    get_url = post_url + '/' + m_id

    r = requests.get(get_url).json()

    # print(j, r, sep='\n')

    assert r['id'] == m_id
    assert r['title'] == m_title
