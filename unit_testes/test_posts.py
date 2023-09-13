import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"
post_data = {
    "title": "Test Post",
    "short_description": "Test Short Description",
    "description": "Test Description",
    "tags": ["tag1", "tag2"],
    "created_at" : "2023-09-13T10:25:53.995000",
    "updated_at" : "2023-09-13T10:25:53.995000"
}
update_data = {
    "title": "Update Test Post",
    "short_description": "Update Test Short Description",
    "description": "Update Test Description",
    "tags": ["Update tag1", "Update tag2"]
}
def test_create_post():
    response = requests.post(f"{BASE_URL}/posts/", json = post_data)
    assert response.status_code == 200
    


def test_get_by_id():
    response = requests.get(f"{BASE_URL}/posts/65016401a80ea658d24878ab")
    assert response.status_code == 200
    assert response.json()['title'] == post_data['title']
    assert response.json()['short_description'] == post_data['short_description']
    assert response.json()['description'] == post_data['description']
    assert response.json()['tags'] == post_data['tags']




def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts/", json = post_data)
    global post
    post = response.json()[-1]
    assert response.status_code == 200


def test_update_post():
    response = requests.put(f"{BASE_URL}/posts/{post['id']}", json = update_data)
    assert response.status_code == 200
    assert response.json()['title'] == update_data['title']
    assert response.json()['short_description'] == update_data['short_description']
    assert response.json()['description'] == update_data['description']
    assert response.json()['tags'] == update_data['tags']



def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/{post['id']}")
    assert response.status_code == 200

