from typing import Dict, List, Optional
from backend.models import Contact
from backend.repository import ContactRepository

class InMemoryContactRepository(ContactRepository):
    def __init__(self):
        self.contacts: Dict[int, Contact] = {}
        self.next_id = 1

    def get_all(self) -> List[Contact]:
        return list(self.contacts.values())

    def get_by_id(self, contact_id: int) -> Optional[Contact]:
        return self.contacts.get(contact_id)

    def create(self, contact: Contact) -> Contact:
        contact.id = self.next_id
        self.contacts[self.next_id] = contact
        self.next_id += 1
        return contact

    def update(self, contact_id: int, updated_contact: Contact) -> Optional[Contact]:
        if contact_id in self.contacts:
            self.contacts[contact_id] = updated_contact
            return updated_contact
        return None

    def delete(self, contact_id: int) -> bool:
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            return True
        return False

    def get_by_email(self, email: str) -> Optional[Contact]:
        for contact in self.contacts.values():
            if contact.email == email:
                return contact
        return None
