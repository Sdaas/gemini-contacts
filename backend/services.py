from pydantic import BaseModel, EmailStr, constr
from typing import List, Dict
from backend.models import Contact


class ContactService:
    def __init__(self):
        self.contacts: Dict[int, Contact] = {}
        self.next_id = 1

    def create_contact(self, contact: Contact) -> Contact:
        contact.id = self.next_id
        self.contacts[self.next_id] = contact
        self.next_id += 1
        return contact

    def get_all_contacts(self) -> List[Contact]:
        return list(self.contacts.values())

    def get_contact_by_id(self, contact_id: int) -> Contact | None:
        return self.contacts.get(contact_id)

    def update_contact(
        self, contact_id: int, updated_contact: Contact
    ) -> Contact | None:
        if contact_id in self.contacts:
            self.contacts[contact_id] = updated_contact
            return updated_contact
        return None

    def delete_contact(self, contact_id: int) -> bool:
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            return True
        return False
