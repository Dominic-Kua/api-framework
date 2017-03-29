"""
Used to be based off a class/method structure
however since nothing was inheriting, I've removed the class
to make it more pythonic
"""

def authorise_payload(username :str, password :str):
    """
    constructs the json for the authorisation payload
    :param username: username string
    :param password: password string
    :return: returns a dictionary of a dictionary of the auth header
    analogous here to json.
    """
    return f'''{{
        "username": {username},
        "password": {password}
    }}'''
