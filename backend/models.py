from pydantic import BaseModel, EmailStr, constr

class Contact(BaseModel):
    id: int
    first_name: constr(min_length=2, pattern=r'^[a-zA-Z]+$')
    last_name: constr(min_length=2, pattern=r'^[a-zA-Z]+$')
    email: EmailStr
    phone_number: str
