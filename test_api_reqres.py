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
        assert r.json()['data']['id'] == 1

def test_update_user():
    with allure.step('Обновление данных УЗ'):
        id_user = '/7'
        first_name = 'Slava'
        email = 'slavaslava@mail.ru'
        last_name = 'Beza'
        r = requests.get(f'{base_url}{path_users}{id_user}',json={'first_name': first_name, 'last_name': last_name, 'email': email})
        logging.info(r.json())
        assert r.status_code == 200

def test_delete_user():
    with allure.step('Удаление УЗ'):
        id_user = '/7'
        r = requests.delete(f'{base_url}{path_users}{id_user}')
        assert r.status_code == 204
        assert r.text == ""

def test_reg_successful():
    with allure.step('Заведение УЗ успешное'):
        email = 'eve.holt@reqres.in'
        passw ='qwerty'
        iden = 4
        token = 'QpwL5tke4Pnpja7X4'
        r = requests.post(f'{base_url}{path_register}', json={'email': email, 'password': passw})
        logging.info(r.json())
        assert r.status_code == 200
        assert r.json()['id'] == iden
        assert r.json()['token'] == token

def test_wrong_reg():
    with allure.step("Ошибка регистрации"):
        email = 'sydney@fife'
        error_message = 'Missing password'
        r = requests.post(f'{base_url}{path_register}', json={'email': email})
        logging.info(r.json())
        assert r.status_code == 400
        assert r.status_code == requests.codes.bad_request
        assert r.json()['error'] == error_message

def test_login_successful():
    with allure.step('Авторизация'):
        email = 'eve.holt@reqres.in'
        passw = 'qwerty'
        token = 'QpwL5tke4Pnpja7X4'
        r = requests.post(f'{base_url}{path_login}', json={'email': email, 'password': passw})
        logging.info(r.json())
        assert r.status_code == requests.codes.ok
        assert r.json()['token'] == token

def test_wrong_login():
    with allure.step("Ошибка авторизации"):
        email = 'peter@klaven'
        error_message = 'Missing password'
        r = requests.post(f'{base_url}{path_register}', json={'email': email})
        logging.info(r.json())
        assert r.status_code == 400
        assert r.status_code == requests.codes.bad_request
        assert r.json()['error'] == error_message

def test_delayed_response():
    with allure.step('Delyaed presponse'):
        delay = 3
        r = requests.get(f'{base_url}{path_users }', params={'delay': delay})
        logging.info(r.json())
        assert r.status_code == 200
        assert r.json()['total'] == 12
        assert r.json()["total_pages"] == 2


