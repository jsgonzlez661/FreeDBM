from app.resource import *

class Logout(Resource):

	def get(self):
		cookies = request.cookies
		if(cookies != {}):
			responds = {
				"status": "success",
				"message": "Successfully logged out"
			}
			resp = make_response(responds)			
			resp.set_cookie('auth_token', cookies['auth_token'], expires = 0)
			return resp
		else:
			responds = {
				"status": "success",
				"message": "User is not login"
			}
			return responds, 200