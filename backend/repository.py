from abc import ABC, abstractmethod
from typing import List, Optional
from backend.models import Contact

class ContactRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Contact]:
        pass

    @abstractmethod
    def get_by_id(self, contact_id: int) -> Optional[Contact]:
        pass

    @abstractmethod
    def create(self, contact: Contact) -> Contact:
        pass

    @abstractmethod
    def update(self, contact_id: int, updated_contact: Contact) -> Optional[Contact]:
        pass

    @abstractmethod
    def delete(self, contact_id: int) -> bool:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Contact]:
        pass
