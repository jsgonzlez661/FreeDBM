from app.resource import *

class Login(Resource):

	def post_login(self):

		"""esta fucncionalidad se encarga de hacer la petición post para validar el usuario existente"""

		jsonfile = request.get_json()
		auth_token = jsonfile.get('auth_token')

		try:
			decoded = jwt.decode(auth_token, config.KEY, algorithm = 'HS256')
		except jwt.exceptions.DecodeError:
			responds = {
				"status": 401,
				"message": "Provide a valid auth token",
			}			
			return responds, responds['status']
		else: 
			email = decoded['email']
			password = decoded['password'].encode('utf-8')

			query = select( [ User ] ).where( User.email == email )
			result = db.session.execute(query)
			user = result.fetchone()


		if user != None and len(user) > 0:
			if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):

				responds = {
					"status": 200,
					"message": "Successfully logged in",
					"auth_token": auth_token
				}

				response = make_response(responds)
				response.set_cookie("auth_token", auth_token)

				return response, responds['status']
			
			else:
				responds = {
				"status": 400,
				"message": "Error Password User Not math",
				}			
			return responds, responds['status']		

		else:
			responds = {
				"status": 400,
				"message": "Provide a valid auth token",
			}			
			return responds, responds['status']		


	def get_cookies_session(self):
		cookies = request.cookies
		if( cookies ==  {} ):
			responds = {
				"status": 401,
				"message": "User is not login"
			}
			return responds, responds['status']		
		else:
			responds = {
				"status": 200,
				"message": "User is logged in",
			}			
			return responds, responds['status']	
