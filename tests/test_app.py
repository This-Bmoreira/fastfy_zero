from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_should_ok_and_hello_wold():
    client = TestClient(app)  # Organização do test
    response = client.get('/')  # ação
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá mundo'}  # assert
