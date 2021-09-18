from app import app 

def test_hello_name():
    response = app.test_client().get('/hello/reuben')

    assert response.status_code == 200
    assert response.data == b'Hello, reuben'



def test_universe():
    response = app.test_client().get('/universe')

    assert response.status_code == 200
    assert response.data == b'42'