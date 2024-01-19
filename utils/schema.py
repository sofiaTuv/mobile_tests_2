from pytest_voluptuous import S

item_create = S({
    'method': str,
    'status': str,
    'result': {
        'id': str,
        'name': str,
        'section': str,
        'description': str,
        'color': str,
        'size': str,
        'price': int,
        'params': str,
    },
})

item_get = S({
    'method': str,
    'status': str,
    'result': {
        'id': str,
        'name': str,
        'section': str,
        'description': str,
        'color': str,
        'size': str,
        'price': int,
        'params': str,
        'photo': str
    },
})

item_update = S({
    'method': str,
    'status': str,
    'result': str,
})

items_search = S({
    "method": str,
    "status": str,
    "result": [
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        },
        {
            "last_id": str,
            "title": str
        }
    ]
})

item_delete = S({
    'method': str,
    'status': str,
    'result': str
})