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


access_token = '78TGcsSSyJirRQd1Va19BZMK4wrmDAyTJiTDZaeo6C5R4k5rE7uOhwNHtyA0rHt2kfXdZ54qPqdRNsvNFFC1iSNWZPncU1QKcEGK7sf6wPrgwks1mInTQsfpyh6OM88TebvnTboqqlT0LbCbgwlORRv97p71g7HcWuK24zXIMRWTq8P8ha5ts9uZMM5cEKvnCUq0yxe7IltfSnxPZfl8ngprhD3ZnYPHpNHesGFDvk64oUNYZZP1WbXEXFcUxtpD'


headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}


def get_account_information_with_oauth():
    # Now attempt to get the logged-in user's data
    print '\nATTEMPTING TO GET ACCOUNT INFORMATION WITH OAUTH'
    account_details_url = 'http://localhost:1337/test_login'
    print 'target url is %s' % account_details_url
    req2 = urllib2.Request(account_details_url, None, headers)
    try:
        resp2 = urllib2.urlopen(req2)
        print 'successfully got response'
        #d = json.loads(resp2.read())
        #print 'you are %s' % d['user']['email']
    except urllib2.HTTPError as e:
        print 'could not get target'
        #text = e.read()

# now check console log for tresults
get_account_information_with_oauth()

