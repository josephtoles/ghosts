/**
 * oauthBearer policy
 *
 * @module      :: Policy
 * @description :: Simple policy to allow any authenticated user
 *                 Assumes that your login action in one of your controllers sets `req.session.authenticated = true;`
 * @docs        :: http://sailsjs.org/#!documentation/policies
 *
 */

var passport = require('passport');

module.exports = function(req, res, next) {

    console.log('hit oauthBearer policy');

	passport.authenticate(
	    'bearer',
	    function(err, user, info)
	    {
	        if ((err) || (!user))
	        {
                console.log('user is '+user);
                console.log('info is '+info);
	            res.send(401);
	            // res.redirect('/');
	            return;
	        }
            delete req.query.access_token;
            console.log('req.user ASSIGNED');
	        req.user = user;
	        return next();
	    }
	)(req, res);
};
