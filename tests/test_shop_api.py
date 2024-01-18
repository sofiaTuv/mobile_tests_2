import allure
import pytest

from page.schema import item_create, item_get, item_update, items_search, item_delete
from page.shopbugred_api import TestShopBugredAPI
from pytest_voluptuous import S

pytest.item_id = None


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 's.tuvykina')
@allure.story('Создаем товар')
def test_create_item():
    result = TestShopBugredAPI.api_request('create/', data={
        "name": "Шортики",
        "section": "Платья",
        "description": "Модное платье из новой коллекции!",
        "color": "RED",
        "size": 44,
        "price": 666,
        "params": "dress"
    })
    data = result.json()

    with allure.step('Статус код=200'):
        assert result.status_code == 200
    with allure.step('Проверка схемы'):
        assert data == S(item_create)
    with allure.step('Проверка статуса'):
        assert str(data['status']) == 'ok'
    with allure.step('Проверка названия'):
        assert str(data['result']['name']) == 'Шортики'
    with allure.step('Проверка секции'):
        assert str(data['result']['section']) == 'Платья'
    with allure.step('Проверка описания'):
        assert str(data['result']['description']) == 'Модное платье из новой коллекции!'
    with allure.step('Проверка цвета'):
        assert str(data['result']['color']) == 'RED'
    with allure.step('Проверка размера'):
        assert str(data['result']['size']) == '44'
    with allure.step('Проверка цены'):
        assert str(data['result']['price']) == '666'
    with allure.step('Проверка категории'):
        assert str(data['result']['params']) == 'dress'
    pytest.item_id = data['result']['id']


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 's.tuvykina')
@allure.story('ID товара, по которому мы хотим получить информацию')
def test_get_item_id():
    result = TestShopBugredAPI.api_request('get/', data={
        "id": f'{pytest.item_id}'
    })
    data = result.json()

    with allure.step('Статус код=200'):
        assert result.status_code == 200
    with allure.step('Проверка id'):
        assert str(data['result']['id']) == f'{pytest.item_id}'
    with allure.step('Проверка схемы'):
        assert data == S(item_get)
    with allure.step('Проверка статуса'):
        assert str(data['status']) == 'ok'
    with allure.step('Проверка названия'):
        assert str(data['result']['name']) == 'Шортики'
    with allure.step('Проверка секции'):
        assert str(data['result']['section']) == 'Платья'
    with allure.step('Проверка описания'):
        assert str(data['result']['description']) == 'Модное платье из новой коллекции!'
    with allure.step('Проверка размера'):
        assert str(data['result']['size']) == '44'
    with allure.step('Проверка цвета'):
        assert str(data['result']['color']) == 'RED'


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 's.tuvykina')
@allure.story('ID товара, который мы хотим обновить')
def test_update_item():
    result = TestShopBugredAPI.api_request('update/', data={
        "id": f'{pytest.item_id}',
        "name": "Легкое платье",
        "section": "Платья",
        "description": "Из старой коллекции!",
        "color": "GREEN",
        "size": 48,
        "price": 2999,
        "params": "dress",
    })
    data = result.json()

    with allure.step('Статус код=200'):
        assert result.status_code == 200
    with allure.step('Проверка схемы'):
        assert data == S(item_update)
    with allure.step('Проверка статуса'):
        assert str(data['status']) == 'ok'
    with allure.step('Проверка результата'):
        assert str(data['result']) == 'Товар обновлен!'


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 's.tuvykina')
@allure.story('Поиск карточек товара')
def test_search_items():
    result = TestShopBugredAPI.api_request('search/', data={
        "query": "Шортики"
    })
    data = result.json()

    with allure.step('Статус код=200'):
        assert result.status_code == 200
    with allure.step('Проверка схемы'):
        assert data == S(items_search)
    with allure.step('Проверка статуса'):
        assert str(data['status']) == 'ok'


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 's.tuvykina')
@allure.story('ID товара, который мы хотим удалить')
def test_delete_item():
    result = TestShopBugredAPI.api_request('/delete', data={
        "id": f'{pytest.item_id}'
    })
    data = result.json()

    with allure.step('Статус код=200'):
        assert result.status_code == 200
    with allure.step('Проверка схемы'):
        assert data == S(item_delete)
    with allure.step('Проверка статуса'):
        assert str(data['status']) == 'ok'
    with allure.step('Проверка результата'):
        assert str(data['result']) == f'Товар с ID {pytest.item_id} успешно удален'
