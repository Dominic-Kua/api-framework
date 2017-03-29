import json
from api.booking import *
from api.authorise import *
from payloads.booking_payload import booking_payload
from payloads.authorise_payload import authorise_payload


def test_get_booking():
    response = all_bookings()
    assert response.status_code == 200


def test_get_specific_booking():
    response = specific_booking(1, 'application/json')
    assert response.status_code == 200


def test_get_returns_418_with_bad_heading():
    response = specific_booking(1, 'text/html')
    assert response.status_code == 418


def test_post_returns_200():
    payload = booking_payload('Sally',
                             'Anne',
                             123,
                             'true',
                             '2016-01-01',
                             '2016-01-02',
                             'breakfast')

    response = create_booking(payload, 'application/json')
    assert response.status_code == 200


def test_delete_booking():
    payload = booking_payload('Sally',
                             'Anne',
                             123,
                             'true',
                             '2016-01-01',
                             '2016-01-02',
                             'breakfast')

    created_response = create_booking(payload, 'application/json')
    payload_id = json.loads(created_response.content)['bookingid']

    auth_payload = authorise_payload('admin',
                                    'password123')
    auth_response = post_credentials(payload)
    print(auth_response.content)

    auth_token = json.loads(auth_response.content)['token']

    delete_response = delete_booking(payload_id, auth_token)
    assert delete_response.status_code == 201

