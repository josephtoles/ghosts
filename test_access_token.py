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


access_token = '2AYrqheduWAYAp5JK92MJq5PYRizHhwKRIfiumVvhznz30pF1fPguFvBNtPeRKasTfpoax3hpsGqZVy1gBJTO31MQbAeuRG1fReWYXTvKijaBw23vYe1W2WpyRuDnPzJf6HRiOAzTmuZttJ2YVbSibwEkLi0nc3q8EDbGWYYZSaCyfRILCUUjYPfBNWqRtR3KkCb3JdMvXDDdxdeMJP295NgIJsTcwF6XGrVm1OWuC3pn3hn6KIQkcFWu4jtw8BA'


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

