from app.resource import *

class Login(Resource):

	def post(self):
		jsonfile = request.get_json()
		auth_token = jsonfile.get('auth_token')

		try:
			decoded = jwt.decode(auth_token, config.KEY, algorithm = 'HS256')
		except jwt.exceptions.DecodeError:
			responds = {
				"status": "fail",
				"message": "Provide a valid auth token",
			}			
			return responds, 401	

		email = decoded['email']
		password = decoded['password'].encode('utf-8')

		query = select([User]).where(User.email == email)
		result = db.session.execute(query)
		user = result.fetchone()

		if user != None and len(user) > 0:
			if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
				responds = {
					"status": "success",
					"message": "Successfully logged in",
					"auth_token": auth_token
				}
				resp = make_response(responds)
				resp.set_cookie("auth_token", auth_token)
				return resp
			else:
				responds = {
				"status": "fail",
				"message": "Error Password User Not math",
			}			
			return responds, 401
		else:
			responds = {
				"status": "fail",
				"message": "Provide a valid auth token",
			}			
			return responds, 401		


	def get(self):
		cookies = request.cookies
		if(cookies == {}):
			responds = {
				"status": "success",
				"message": "User is not login"
			}
			return responds, 200
		else:
			responds = {
				"status": "success",
				"message": "User is logged in",
			}			
			return responds, 200

