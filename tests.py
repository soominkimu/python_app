from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello Soomin!'
    assert response.status_code == 200
