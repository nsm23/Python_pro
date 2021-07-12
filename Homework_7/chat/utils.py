from datetime import datetime

TIME = datetime.now()

RESPONSE = {
    "response": None,
    "time": str(TIME),
    "alert": None,
}

PRESENCE = {
    "action": "presence",
    "time": str(TIME),
    "user": {
        "account_name": '',
        "status": "Online!"
    }
}

MESSAGE = {
    "action": "msg",
    "time": str(TIME),
}


SERVER_RESP = (
    ('200', 'Ok!'),
    ('404', 'Not found'),
    ('401', 'Error authitication')
)