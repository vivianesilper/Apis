from flask.testing import FlaskClient


def test_get_purchase_orders(test_client: FlaskClient):
    response = test_client.get('/purchase_orders')
    
    assert response.status_code == 200
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'Purchase Order id 1'
    assert len(response.json[0]['items']) == 1
    assert response.json[0]['items'][0]['id'] == 1
    
def test_post_purchase_orders(test_client):