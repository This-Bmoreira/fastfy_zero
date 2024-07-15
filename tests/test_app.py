from http import HTTPStatus


def test_read_root_should_ok_and_hello_wold(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'fake-user',
            'password': 'fake-password',
            'email': 'fake-email@test.com',
        },
    )  # ação
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'fake-user',
        'email': 'fake-email@test.com',
    }  # assert


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'fake-user',
                'email': 'fake-email@test.com',
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'fake-user-update',
            'password': 'fake-password',
            'email': 'fake-email@test.com',
        },
    )

    assert response.json() == {
        'id': 1,
        'username': 'fake-user-update',
        'email': 'fake-email@test.com',
    }


def test_delete_users(client):
    response = client.delete(
        '/users/1'
    )

    assert response.json() == {'message': 'User deleted'}
