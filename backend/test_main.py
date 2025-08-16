from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '.')

from main import app

client = TestClient(app)

def test_create_contact():
    response = client.post("/contacts/", json={"id": 0, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "phone_number": "1234567890"})
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["email"] == "john.doe@example.com"
    assert data["phone_number"] == "1234567890"
    assert "id" in data

def test_list_contacts():
    response = client.get("/contacts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_contact():
    # Create a contact first
    response = client.post("/contacts/", json={"id": 0, "first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com", "phone_number": "0987654321"})
    contact_id = response.json()["id"]

    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Jane"

def test_update_contact():
    # Create a contact first
    response = client.post("/contacts/", json={"id": 0, "first_name": "Jake", "last_name": "Doe", "email": "jake.doe@example.com", "phone_number": "1122334455"})
    contact_id = response.json()["id"]

    response = client.put(f"/contacts/{contact_id}", json={"id": contact_id, "first_name": "Jake", "last_name": "Smith", "email": "jake.smith@example.com", "phone_number": "5544332211"})
    assert response.status_code == 200
    data = response.json()
    assert data["last_name"] == "Smith"

def test_delete_contact():
    # Create a contact first
    response = client.post("/contacts/", json={"id": 0, "first_name": "Josh", "last_name": "Doe", "email": "josh.doe@example.com", "phone_number": "6677889900"})
    contact_id = response.json()["id"]

    response = client.delete(f"/contacts/{contact_id}")
    assert response.status_code == 200

    # Verify it's deleted
    response = client.get(f"/contacts/{contact_id}")
    assert response.status_code == 404
