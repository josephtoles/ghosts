CLIENT_ID=KCX65QW3W0
CLIENT_SECRET=f8ZUYL4v4QuaBhSL44MTnyOdxSCLxg
curl -XPOST -d 'client_id='$CLIENT_ID'&client_secret='$CLIENT_SECRET'&grant_type=authorization_code&redirect_uri=REDIRECT_URI&code=CODE' http://localhost:1337/oauth/token

