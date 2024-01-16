def test_read_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_say_hello(test_client):
    response = test_client.get("/say_hello")
    assert response.status_code == 200
    assert response.text == f"Hello {None}"


def test_update_user(test_client):
    user = {"name": "test_user", "is_awesome": True}
    response = test_client.put("/users/new", json=user)
    assert response.status_code == 200
    assert response.json() == {"name": user["name"], "is_awesome": user["is_awesome"]}


def test_update_user_than_say_hello(test_client):
    user = {"name": "test_user", "is_awesome": True}
    response = test_client.put("/users/new", json=user)
    assert response.status_code == 200

    response = test_client.get("/say_hello")
    assert response.status_code == 200
    assert response.text == f"Hello {user['name']}"
