"""
Used to be based off a class/method structure
however since nothing was inheriting, I've removed the class
to make it more pythonic.
"""

def booking_payload(firstname :str, lastname : str, totalprice :float, depositpaid :str, checkin :str, checkout :str, additionalneeds :str):
    """

    :param firstname:
    :param lastname:
    :param totalprice:
    :param depositpaid:
    :param checkin:
    :param checkout:
    :param additionalneeds:
    :return:
    """
    return f"""{{
        "firstname": "{firstname}",
        "lastname": "{lastname}",
        "totalprice": {totalprice},
        "depositpaid": {depositpaid},
        "bookingdates": {{
            "checkin": "{checkin}",
            "checkout": "{checkout}"
        }},
        "additionalneeds": "{additionalneeds}"
    }}"""
