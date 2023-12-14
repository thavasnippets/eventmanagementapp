
updateSchema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "tag": {
            "type": "string"
        },
        "organiser": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "email": {
                    "type": "string",
                    "pattern": "^\\S+@\\S+\\.\\S+$",
                    "format": "email",
                    "minLength": 6,
                    "maxLength": 127

                },
                "phone": {
                    "type": "string",
                    "minLength": 10,
                    "maxLength": 10
                }
            },
            "required": [
                "name",
                "email"
            ]

        },
        "tollfree": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10
        },
        "helpdeskemail": {
            "type": "string",
            "pattern": "^\\S+@\\S+\\.\\S+$",
            "format": "email",
            "minLength": 6,
            "maxLength": 127

        },
        "address": {
            "type": "object",
            "properties": {
                "line1": {
                    "type": "string"
                },
                "line2": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "country": {
                    "type": "string"
                },
                "pin": {
                    "type": "string"
                }
            },
            "required": [
                "line1",
                "city",
                "country",
                "pin"
            ]
        }
    },
    "required": [
        "name",
        "organiser",
        "address"
    ]

}
