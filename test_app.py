from app import app 

def test_add_numbers():
    response = app.test_client().get('/add/3/2')

    assert response.status_code == 200
    assert response.data == b'5'



def test_universe():
    response = app.test_client().get('/universe')

    assert response.status_code == 200
    assert response.data == b'42'