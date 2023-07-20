import pytest
import allure
import requests
from requests import Response
import logging

base_url = 'https://reqres.in'
path_users = '/api/users'
path_register = '/api/register'
path_login = '/api/login'



def test_open_page():
    with allure.step('открываем страницу'):

        response = requests.get(f'{base_url}{path_users }', params={'page': 1})
        logging.info(response.json())
        assert response.status_code == 200

def test_create_user():
    with allure.step('Добавляем УЗ'):
        response = requests.post(f'{base_url}{path_users}', json={'first_name': 'David', 'avatar': 'Apple'})
        logging.info(response.json())
        assert response.status_code == 201
        assert response.json()['first_name'] == 'David'

def test_dict_user ():
    with allure.step("Проверка списка"):
        dict_element = 5
        r = requests.get(f'{base_url}{path_users}', params={'id': 1})
        logging.info(r.json())
        assert r.status_code == 200
        assert len(r.json()['data']) == dict_element

