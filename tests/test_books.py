def create_books(client):
    response = client.post("/books",json={"title":"hello","author":"tajik","genre":"music","available":False})
    assert response.status_code == 201
def all_books(client):
    response = client.get("/books")
    return response.status_code == 200
def get_book(client):
    response = client.get("/books/1")
    assert response.status_code == 200
def update_book(client):
    response = client.put("/books/1",json={"title":"anime"})
    assert response.status_code == 201
def delete_book(client):
    response = client.delete("/books/1")
    assert response.status_code == 200
    