from fastapi.testclient import TestClient
from backend.main import app, contact_repository
from backend.in_memory_repository import InMemoryContactRepository
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_db():
    print(f"Resetting DB. Before: {contact_repository.contacts}, {contact_repository.next_id}")
    contact_repository.contacts = {}
    contact_repository.next_id = 1
    yield
    print(f"Resetting DB. After: {contact_repository.contacts}, {contact_repository.next_id}")

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

def test_create_contact_invalid_email():
    response = client.post("/contacts/", json={"id": 0, "first_name": "John", "last_name": "Doe", "email": "john.doe", "phone_number": "1234567890"})
    assert response.status_code == 422

def test_create_contact_invalid_first_name_too_short():
    response = client.post("/contacts/", json={"id": 0, "first_name": "J", "last_name": "Doe", "email": "john.doe@example.com", "phone_number": "1234567890"})
    assert response.status_code == 422

def test_create_contact_invalid_first_name_not_alpha():
    response = client.post("/contacts/", json={"id": 0, "first_name": "John1", "last_name": "Doe", "email": "john.doe@example.com", "phone_number": "1234567890"})
    assert response.status_code == 422

def test_create_contact_invalid_last_name_too_short():
    response = client.post("/contacts/", json={"id": 0, "first_name": "John", "last_name": "D", "email": "john.doe@example.com", "phone_number": "1234567890"})
    assert response.status_code == 422

def test_create_contact_invalid_last_name_not_alpha():
    response = client.post("/contacts/", json={"id": 0, "first_name": "John", "last_name": "Doe1", "email": "john.doe@example.com", "phone_number": "1234567890"})
    assert response.status_code == 422

def test_create_contact_duplicate_email():
    # Create a contact first
    response = client.post("/contacts/", json={"id": 0, "first_name": "Duplicate", "last_name": "Email", "email": "duplicate@example.com", "phone_number": "1111111111"})
    assert response.status_code == 200

    # Try to create another with the same email
    response = client.post("/contacts/", json={"id": 0, "first_name": "Another", "last_name": "One", "email": "duplicate@example.com", "phone_number": "2222222222"})
    assert response.status_code == 409 # Conflict

def test_update_contact_duplicate_email():
    # Create two contacts
    response1 = client.post("/contacts/", json={"id": 0, "first_name": "UpdateOne", "last_name": "Test", "email": "update1@example.com", "phone_number": "1111111111"})
    print(f"Response1 status: {response1.status_code}, json: {response1.json()}")
    contact_id1 = response1.json()["id"]

    response2 = client.post("/contacts/", json={"id": 0, "first_name": "UpdateTwo", "last_name": "Test", "email": "update2@example.com", "phone_number": "2222222222"})
    contact_id2 = response2.json()["id"]

    # Try to update contact1's email to contact2's email
    response = client.put(f"/contacts/{contact_id1}", json={"id": contact_id1, "first_name": "UpdateOne", "last_name": "Test", "email": "update2@example.com", "phone_number": "1111111111"})
    assert response.status_code == 409 # Conflict
