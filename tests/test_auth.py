def test_register(client):
    response = client.post("/auth/register",json={"email":"bakjiya@gmail","password":"tajik"})
    assert response.status_code == 201

def test_dup(client):
    response = client.post("/auth/register",json={"email":"bakjiya@gmail","password":"tajik"})
    assert response.status_code == 400
def test_login(client):
    response = client.post("/auth/login",data={"username":"chasmis@gmail.com","password":"tajik"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
def test_wrong_password(client):
    response = client.post("/auth/login",data={"username":"chasmis@gmail.com","password":"hello"})
    assert response.status_code == 401