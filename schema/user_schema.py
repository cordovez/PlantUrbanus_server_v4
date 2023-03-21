def user_serializer(user) -> dict:
    """ Returns a single user from collection """
    return {
        'id': str(user['_id']),
        "name": user["name"],
        'role': user["role"]
    }


def users_serializer(users) -> list:
    """ Returns a list of users from collection """
    return [user_serializer(user) for user in users]
