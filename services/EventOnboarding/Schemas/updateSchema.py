schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "tag": {
            "type": "string"
        },
        "status": {
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
        "id",
        "name",
        "organiser",
        "address"
    ]
}

deleteSchema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "id": "1234567890"
        }
    ],
    "required": [
        "id"
    ],
    "properties": {
        "id": {
            "$id": "#/properties/id",
            "type": "string",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1234567890"
            ]
        }
    },
    "additionalProperties": False
}

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
