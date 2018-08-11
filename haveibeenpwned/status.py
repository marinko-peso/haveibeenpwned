# -*- coding: utf-8 -*-
import urllib3


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
    Get back full response.
    :param email: {String}
    :return: {String}
    """
    response = _get_response(email)
    return response.data if response.data else None
