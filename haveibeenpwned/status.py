# -*- coding: utf-8 -*-
import urllib3, json


# Supress warning about insecure request.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
_pwned_url = 'https://haveibeenpwned.com/api/v2/breachedaccount/'
_headers = {'user-agent': 'Pwnage-Checker-PyPi-Package'}


def _get_response(email):
    """
    :param email: {String}
    :return: {String}
    """
    return urllib3.PoolManager().urlopen('GET', '{}{}'.format(_pwned_url, email), headers=_headers)


def pwned(email):
    """
    If we get anything in response its pwned.
    :param email: {String}
    :return: {Boolean}
    """
    response = _get_response(email)
    return True if response.data else False


def pwned_full(email):
    """
    Get back full response decoded from json to dict.
    :param email: {String}
    :return: {Dict}
    """
    response = _get_response(email)
    data = []
    if response.data:
        data = json.loads(response.data)
    return {
        'status': bool(data),
        'data': data
    }
