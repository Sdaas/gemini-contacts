import React from 'react';

function ContactDetails({ contact, onDelete }) {
    if (!contact) {
        return <div>Select a contact to see details</div>;
    }

    return (
        <div>
            <h2>Contact Details</h2>
            <p><strong>First Name:</strong> {contact.first_name}</p>
            <p><strong>Last Name:</strong> {contact.last_name}</p>
            <p><strong>Email:</strong> {contact.email}</p>
            <p><strong>Phone Number:</strong> {contact.phone_number}</p>
            <button onClick={() => onDelete(contact.id)}>Delete</button>
        </div>
    );
}

export default ContactDetails;
