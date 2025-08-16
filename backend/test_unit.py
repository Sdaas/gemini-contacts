import pytest
from backend.services import ContactService, DuplicateEmailError
from backend.models import Contact
from backend.repository import ContactRepository
from backend.in_memory_repository import InMemoryContactRepository

@pytest.fixture
def contact_service():
    repository = InMemoryContactRepository()
    return ContactService(repository)

def test_create_contact(contact_service: ContactService):
    contact = Contact(id=0, first_name="Julius", last_name="Caesar", email="jc@rome.com", phone_number="12345")
    created_contact = contact_service.create_contact(contact)
    assert created_contact.id == 1
    assert created_contact.first_name == "Julius"

def test_get_all_contacts(contact_service: ContactService):
    contact1 = Contact(id=0, first_name="Julius", last_name="Caesar", email="jc@rome.com", phone_number="12345")
    contact2 = Contact(id=0, first_name="Marcus", last_name="Aurelius", email="ma@rome.com", phone_number="67890")
    contact_service.create_contact(contact1)
    contact_service.create_contact(contact2)
    contacts = contact_service.get_all_contacts()
    assert len(contacts) == 2
    assert contacts[0].first_name == "Julius"
    assert contacts[1].first_name == "Marcus"

def test_get_contact_by_id(contact_service: ContactService):
    contact = Contact(id=0, first_name="Julius", last_name="Caesar", email="jc@rome.com", phone_number="12345")
    created_contact = contact_service.create_contact(contact)
    retrieved_contact = contact_service.get_contact_by_id(created_contact.id)
    assert retrieved_contact is not None
    assert retrieved_contact.first_name == "Julius"

def test_get_contact_by_id_not_found(contact_service: ContactService):
    retrieved_contact = contact_service.get_contact_by_id(999)
    assert retrieved_contact is None

def test_update_contact(contact_service: ContactService):
    contact = Contact(id=0, first_name="Julius", last_name="Caesar", email="jc@rome.com", phone_number="12345")
    created_contact = contact_service.create_contact(contact)
    updated_data = Contact(id=created_contact.id, first_name="Gaius", last_name="Julius", email="gjc@rome.com", phone_number="54321")
    updated_contact = contact_service.update_contact(created_contact.id, updated_data)
    assert updated_contact is not None
    assert updated_contact.first_name == "Gaius"
    assert updated_contact.last_name == "Julius"

def test_update_contact_not_found(contact_service: ContactService):
    updated_data = Contact(id=999, first_name="Gaius", last_name="Julius", email="gjc@rome.com", phone_number="54321")
    updated_contact = contact_service.update_contact(999, updated_data)
    assert updated_contact is None

def test_delete_contact(contact_service: ContactService):
    contact = Contact(id=0, first_name="Julius", last_name="Caesar", email="jc@rome.com", phone_number="12345")
    created_contact = contact_service.create_contact(contact)
    result = contact_service.delete_contact(created_contact.id)
    assert result is True
    assert contact_service.get_contact_by_id(created_contact.id) is None

def test_delete_contact_not_found(contact_service: ContactService):
    result = contact_service.delete_contact(999)
    assert result is False

def test_get_by_email(contact_service: ContactService):
    contact1 = Contact(id=0, first_name="Julius", last_name="Caesar", email="jc@rome.com", phone_number="12345")
    contact_service.create_contact(contact1)
    retrieved_contact = contact_service.repository.get_by_email("jc@rome.com")
    assert retrieved_contact is not None
    assert retrieved_contact.email == "jc@rome.com"

def test_get_by_email_not_found(contact_service: ContactService):
    retrieved_contact = contact_service.repository.get_by_email("nonexistent@example.com")
    assert retrieved_contact is None

def test_create_contact_duplicate_email(contact_service: ContactService):
    contact1 = Contact(id=0, first_name="Julius", last_name="Caesar", email="duplicate@example.com", phone_number="12345")
    contact_service.create_contact(contact1)
    contact2 = Contact(id=0, first_name="Marcus", last_name="Aurelius", email="duplicate@example.com", phone_number="67890")
    with pytest.raises(DuplicateEmailError):
        contact_service.create_contact(contact2)

def test_update_contact_duplicate_email(contact_service: ContactService):
    contact1 = Contact(id=0, first_name="Julius", last_name="Caesar", email="unique1@example.com", phone_number="12345")
    contact2 = Contact(id=0, first_name="Marcus", last_name="Aurelius", email="unique2@example.com", phone_number="67890")
    created_contact1 = contact_service.create_contact(contact1)
    created_contact2 = contact_service.create_contact(contact2)

    updated_data = Contact(id=created_contact1.id, first_name="Julius", last_name="Caesar", email="unique2@example.com", phone_number="12345")
    with pytest.raises(DuplicateEmailError):
        contact_service.update_contact(created_contact1.id, updated_data)
