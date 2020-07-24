from app.resource import *

class Logout(Resource):

	def get_cookies_logout(self):

		cookies = request.cookies

		if( cookies  !=  {} ):
			responds = {
				"status": 200,
				"message": "Successfully logged out"
			}

			response = make_response(responds)			
			response.set_cookie( 'auth_token',  cookies['auth_token'],  expires = 0)

			return response
		else:
			responds = {
				"status": 200,
				"message": "User is not login"
			}
			return responds, responds['status']
			