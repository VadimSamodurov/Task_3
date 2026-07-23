import uuid

import requests

API_BASE = 'https://stellarburgers.education-services.ru/api'


def generate_user_data():
    unique = uuid.uuid4().hex[:10]
    return {
        'email': f'ui_user_{unique}@yandex.ru',
        'password': 'Password123!',
        'name': f'UI User {unique}',
    }


def create_user():
    payload = generate_user_data()
    response = requests.post(f'{API_BASE}/auth/register', json=payload)
    access_token = response.json().get('accessToken')
    return payload, access_token


def delete_user(access_token):
    if access_token:
        requests.delete(f'{API_BASE}/auth/user', headers={'Authorization': access_token})


def get_ingredient_ids():
    response = requests.get(f'{API_BASE}/ingredients')
    ingredients = response.json()['data']
    bun = next(item['_id'] for item in ingredients if item['type'] == 'bun')
    filling = next(item['_id'] for item in ingredients if item['type'] == 'main')
    return [bun, filling]


def create_order(access_token):
    ingredients = get_ingredient_ids()
    response = requests.post(
        f'{API_BASE}/orders',
        json={'ingredients': ingredients},
        headers={'Authorization': access_token}
    )
    return response.json()
