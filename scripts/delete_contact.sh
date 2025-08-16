#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <contact_id>"
    exit 1
fi

CONTACT_ID=$1

curl -X DELETE http://localhost:8000/contacts/$CONTACT_ID
