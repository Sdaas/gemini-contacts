import React, { useState, useEffect } from 'react';

function ContactForm({ selectedContact, onSave }) {
    const [contact, setContact] = useState({ id: null, first_name: '', last_name: '', email: '', phone_number: '' });

    useEffect(() => {
        if (selectedContact) {
            setContact(selectedContact);
        }
    }, [selectedContact]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setContact(prevContact => ({ ...prevContact, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSave(contact);
        setContact({ id: null, first_name: '', last_name: '', email: '', phone_number: '' });
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>{contact.id ? 'Edit Contact' : 'New Contact'}</h2>
            <input type="text" name="first_name" placeholder="First Name" value={contact.first_name} onChange={handleChange} required />
            <input type="text" name="last_name" placeholder="Last Name" value={contact.last_name} onChange={handleChange} required />
            <input type="email" name="email" placeholder="Email" value={contact.email} onChange={handleChange} required />
            <input type="text" name="phone_number" placeholder="Phone Number" value={contact.phone_number} onChange={handleChange} required />
            <button type="submit">Save</button>
        </form>
    );
}

export default ContactForm;
