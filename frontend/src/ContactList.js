import React, { useState, useEffect } from 'react';

function ContactList({ onSelectContact }) {
    const [contacts, setContacts] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/contacts/')
            .then(response => response.json())
            .then(data => setContacts(data));
    }, []);

    return (
        <div>
            <h2>Contacts</h2>
            <ul>
                {contacts.map(contact => (
                    <li key={contact.id} onClick={() => onSelectContact(contact)}>
                        {contact.first_name} {contact.last_name}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ContactList;
