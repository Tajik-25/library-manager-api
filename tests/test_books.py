def test_docs(client):
    response = client.get("/docs")
    assert response.status_code == 200
def test_openapi(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
def test_create_book(client):
    response = client.post("/books",json={"title":"python","author":"tajik","genre":"programming","available":True})
    assert response.status_code == 401
def test_update_book(client):
    response = client.put("/books/1",json={"title":"java","genre":"ekaar"})
    assert response.status_code == 401
def test_delete_book(client):
    response = client.delete("/books/1")
    assert response.status_code == 401
