# -*- coding: utf-8 -*-
import urllib3


_pwned_url = 'https://haveibeenpwned.com/api/v2/breachedaccount/'
_headers = {'user-agent': 'Pwnage-Checker-PyPi-Package'}


def pwned(email, full_response=False):
    """
    Attempt fetching the response from the service.
    If we get anything its pwned and return True.
    :param email: {List}
    :return: {Boolean}
    """
    response = urllib3.PoolManager().urlopen('GET', '{}{}'.format(_pwned_url, email), headers=_headers)
    return True if response.data else False
