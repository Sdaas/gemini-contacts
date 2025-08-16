from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str

# In-memory database
contacts: Dict[int, Contact] = {}
next_id = 1

@app.post("/contacts/", response_model=Contact)
def create_contact(contact: Contact):
    global next_id
    contact.id = next_id
    contacts[next_id] = contact
    next_id += 1
    return contact

@app.get("/contacts/", response_model=List[Contact])
def list_contacts():
    return list(contacts.values())

@app.get("/contacts/{contact_id}", response_model=Contact)
def get_contact(contact_id: int):
    if contact_id not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contacts[contact_id]

@app.put("/contacts/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, updated_contact: Contact):
    if contact_id not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    contacts[contact_id] = updated_contact
    return updated_contact

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    if contact_id not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    del contacts[contact_id]
    return {"message": "Contact deleted successfully"}
