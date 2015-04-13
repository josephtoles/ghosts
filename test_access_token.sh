#!/usr/bin/env python
import json
import requests
import urllib
import urllib2
import string

# General Constants
EMAIL = 'me@gmail.com'
PASSWORD = 'password'
ROOT_URL = 'http://localhost:1337/oauth/token'
DICT = {'username': EMAIL, 'password': PASSWORD}


oauth_url = ROOT_URL + 'oauth2/access_token/'
DICT = {
    'client_id': 'KCX65QW3W0',
    'username': 'me@gmail.com',
    'password': 'password',
    'grant_type': 'password',
}
data = urllib.urlencode(DICT)


access_token = 'Qa7vLmM0JYcd8v20I7duKrKVv3Ty6xiibjaMGvRr6sM1zc0IBDffgcZxx8AH46yb1trIYEJqHBjzbJzPMy0if8t8TEhrqvYoLyRXEUBMIVm7ehiwhhqZ5Ih8qG8KPxKBpUVgCczcRfCBYN0TBkBJxHu4pgTQIwqdewsqD4oKDR6StIzpQ5LosdmkzLCMM8eUiYM66pfueCnYZdRHMQXCLEHFq0624BSEoP27hFbLPLZ2MMJQIBhvZVUdkrAVow7B'


headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}


def get_account_information_with_oauth():
    # Now attempt to get the logged-in user's data
    print '\nATTEMPTING TO GET ACCOUNT INFORMATION WITH OAUTH'
    account_details_url = ROOT_URL + 'api/users/me/'
    print 'target url is %s' % account_details_url
    req2 = urllib2.Request(account_details_url, None, headers)
    try:
        resp2 = urllib2.urlopen(req2)
        print 'successfully got my account details'
        #d = json.loads(resp2.read())
        #print 'you are %s' % d['user']['email']
    except urllib2.HTTPError as e:
        print 'could not get my account details'
        #text = e.read()


get_account_information_with_oauth()

