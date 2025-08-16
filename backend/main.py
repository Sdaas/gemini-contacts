from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from backend.services import ContactService, DuplicateEmailError
from backend.models import Contact
from backend.repository import ContactRepository
from backend.in_memory_repository import InMemoryContactRepository

app = FastAPI()
contact_repository = InMemoryContactRepository()
contact_service = ContactService(contact_repository)

@app.exception_handler(DuplicateEmailError)
async def duplicate_email_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": str(exc)}
    )

@app.post("/contacts/", response_model=Contact)
def create_contact(contact: Contact):
    return contact_service.create_contact(contact)

@app.get("/contacts/", response_model=List[Contact])
def list_contacts():
    return contact_service.get_all_contacts()

@app.get("/contacts/{contact_id}", response_model=Contact)
def get_contact(contact_id: int):
    contact = contact_service.get_contact_by_id(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.put("/contacts/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, updated_contact: Contact):
    contact = contact_service.update_contact(contact_id, updated_contact)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    if not contact_service.delete_contact(contact_id):
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}
