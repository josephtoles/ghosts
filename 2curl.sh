CLIENT_ID=KCX65QW3W0
CLIENT_SECRET=f8ZUYL4v4QuaBhSL44MTnyOdxSCLxg
USERNAME='me%40gmail.com'  # escaped version of 'me@joltlabs.com'
PASSWORD='password'
curl -XPOST -d 'client_id='$CLIENT_ID'&client_secret='$CLIENT_SECRET'&grant_type=password&username='$USERNAME'&password='$PASSWORD'&redirect_uri=REDIRECT_URI&code=CODE' http://localhost:1337/oauth/token

