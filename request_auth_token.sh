curl -XPOST -H"X-Ovh-Application: a8itoRHJIZRJoWH7" -H "Content-type: application/json" \
https://eu.api.ovh.com/1.0/auth/credential  -d '{
    "accessRules": [
        {
                "method": "GET",
                "path": "/domain/zone/*"
        },
        {
                "method":"PUT",
                "path":"/domain/zone/*"
        }
    ],
    "redirection":""
}'
