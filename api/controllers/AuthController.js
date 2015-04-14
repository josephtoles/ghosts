/**
 * AuthController
 *
 * @module		:: Controller
 * @description	:: Contains logic for handling auth requests.
 */

var passport = require('passport');

module.exports = {

    test_login: function(req,res){
        console.log('hit test_login');
        console.log(req.user);
        console.log(req.isAuthenticated());
        // TODO Figure out how to get user here
        //console.log(req._passport.user);
        //console.log(req.user);  // doesn't work
        return res.send('Returning');
    },

    redirect: function(req,res){
       res.redirect('/oauth/authorize?client_id=1560741564188360&response_type=code&redirect_uri=https://apps.facebook.com/ghostsj');
       return;
    },

	login: function(req,res){

		passport.authenticate(
		    'local',
		    function(err, user, info)
		    {
		        if ((err) || (!user))
		        {
		            res.redirect('/login');
		            return;
		        }
		        // use passport to log in the user using a local method
		        req.logIn(
		            user,
		            function(err)
		            {
		                if (err)
		                {
		                    res.redirect('/login');
		                    return;
		                }
		                res.redirect('/');
		                return;
		            }
		        );
		    }
		)(req, res);
	},

	logout: function(req,res){
		req.logout();
		res.redirect('/');
	}
 
};
