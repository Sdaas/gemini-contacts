import React, { useState } from 'react';
import './App.css';
import ContactList from './ContactList';
import ContactForm from './ContactForm';
import ContactDetails from './ContactDetails';

function App() {
    const [selectedContact, setSelectedContact] = useState(null);

    const handleSelectContact = (contact) => {
        setSelectedContact(contact);
    };

    const handleSaveContact = (contact) => {
        const method = contact.id ? 'PUT' : 'POST';
        const url = contact.id ? `http://localhost:8000/contacts/${contact.id}` : 'http://localhost:8000/contacts/';

        fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(contact),
        })
        .then(response => response.json())
        .then(() => {
            setSelectedContact(null);
            // A better approach would be to update the state without a full reload
            window.location.reload();
        });
    };

    const handleDeleteContact = (contactId) => {
        fetch(`http://localhost:8000/contacts/${contactId}`, {
            method: 'DELETE',
        })
        .then(() => {
            setSelectedContact(null);
            // A better approach would be to update the state without a full reload
            window.location.reload();
        });
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Contact Management</h1>
            </header>
            <main>
                <div className="container">
                    <div className="left-panel">
                        <ContactList onSelectContact={handleSelectContact} />
                    </div>
                    <div className="right-panel">
                        <ContactForm selectedContact={selectedContact} onSave={handleSaveContact} />
                        <hr />
                        <ContactDetails contact={selectedContact} onDelete={handleDeleteContact} />
                    </div>
                </div>
            </main>
        </div>
    );
}

export default App;