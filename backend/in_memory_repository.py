from typing import Dict, List, Optional
from backend.models import Contact
from backend.repository import ContactRepository

class InMemoryContactRepository(ContactRepository):
    def __init__(self):
        self.contacts: Dict[int, Contact] = {}
        self.email_to_id: Dict[str, int] = {}
        self.next_id = 1

    def get_all(self) -> List[Contact]:
        return list(self.contacts.values())

    def get_by_id(self, contact_id: int) -> Optional[Contact]:
        return self.contacts.get(contact_id)

    def create(self, contact: Contact) -> Contact:
        contact.id = self.next_id
        self.contacts[self.next_id] = contact
        self.email_to_id[contact.email] = contact.id
        self.next_id += 1
        return contact

    def update(self, contact_id: int, updated_contact: Contact) -> Optional[Contact]:
        if contact_id in self.contacts:
            old_contact = self.contacts[contact_id]
            if old_contact.email != updated_contact.email:
                del self.email_to_id[old_contact.email]
                self.email_to_id[updated_contact.email] = updated_contact.id
            self.contacts[contact_id] = updated_contact
            return updated_contact
        return None

    def delete(self, contact_id: int) -> bool:
        if contact_id in self.contacts:
            contact_to_delete = self.contacts[contact_id]
            del self.email_to_id[contact_to_delete.email]
            del self.contacts[contact_id]
            return True
        return False

    def get_by_email(self, email: str) -> Optional[Contact]:
        contact_id = self.email_to_id.get(email)
        if contact_id:
            return self.contacts.get(contact_id)
        return None
