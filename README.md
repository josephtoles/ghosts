# sails

a [Sails](http://sailsjs.org) application


# Test with the following
```
$ curl -XPOST "http://localhost:1337/oauth/token" -d 'client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=authorization_code&rediIRECT_URI&code=CODE'
```
It should return 'Unauthorized'


# OAuth2 example and instructions: https://github.com/lucj/sails-oauth2-api

npm install bcryptjs
npm install passport
npm install moment
npm install passport-http-bearer
npm install passport-http
npm install passport-local
npm install passport-oauth2-client-password
npm install oauth2orize
npm install connect-ensure-login
npm install sails-postgresql
