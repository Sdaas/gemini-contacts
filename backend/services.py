from typing import List, Optional
from backend.models import Contact
from backend.repository import ContactRepository

class DuplicateEmailError(Exception):
    pass

class ContactService:
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    def create_contact(self, contact: Contact) -> Contact:
        if self.repository.get_by_email(contact.email):
            raise DuplicateEmailError("Contact with this email already exists")
        return self.repository.create(contact)

    def get_all_contacts(self) -> List[Contact]:
        return self.repository.get_all()

    def get_contact_by_id(self, contact_id: int) -> Optional[Contact]:
        return self.repository.get_by_id(contact_id)

    def update_contact(
        self, contact_id: int, updated_contact: Contact
    ) -> Optional[Contact]:
        existing_contact_with_email = self.repository.get_by_email(updated_contact.email)
        if existing_contact_with_email and existing_contact_with_email.id != contact_id:
            raise DuplicateEmailError("Contact with this email already exists")
        return self.repository.update(contact_id, updated_contact)

    def delete_contact(self, contact_id: int) -> bool:
        return self.repository.delete(contact_id)
