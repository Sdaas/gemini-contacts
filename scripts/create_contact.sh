#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <first_name> <last_name> <email> <phone_number>"
    exit 1
fi

FIRST_NAME=$1
LAST_NAME=$2
EMAIL=$3
PHONE_NUMBER=$4

curl -X POST http://localhost:8000/contacts/ \
-H "Content-Type: application/json" \
-d '{ "id": 0, "first_name": "'$FIRST_NAME'", "last_name": "'$LAST_NAME'", "email": "'$EMAIL'", "phone_number": "'$PHONE_NUMBER'" }'
