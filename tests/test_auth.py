def register_user(client):
    response = client.post("/auth/register",json={"email":"yanu@12","password":"yanu"})
    assert response.status_code == 201
def user_register(client):
    response = client.post("/auth/register",json={"email":"yanu@12","password":"yanu"})
    assert response.status_code == 400
def login_user(client):
    response = client.post("/auth/login",data={"username":"yanu@12","password":"yanu"})
    assert response.status_code == 200
def user_login(client):
    response = client.post("/auth/login",data={"username":"yanu@12","password":"tajik"})
    assert response.status_code == 401
