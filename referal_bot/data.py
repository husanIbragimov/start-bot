users = {
    "112233": {
        "refer_id": "987654",
        "flag": True,
        "user_really_name": "bot"
    },
    "987654": {
        "refer_id": None,
        "flag": True,
        "user_really_name": "bot"
    },
    "223123": {
        "refer_id": "987654",
        "flag": True,
        "user_really_name": "bot"
    },
    "123456": {
        "refer_id": "987654",
        "flag": True,
        "user_really_name": "bot"
    },
    "654321": {
        "refer_id": "987654",
        "flag": True,
        "user_really_name": "bot"
    },
    "777777": {
        "refer_id": "654321",
        "flag": True,
        "user_really_name": "bot"
    }
}


def get_user_ball(user_id):
    ball = 0
    for value in users.values():
        if user_id == value["refer_id"] and value["flag"]:
            ball += 1
    return ball

