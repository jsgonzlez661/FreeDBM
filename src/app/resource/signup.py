from app.resource import *

class Signup(Resource):
	"""funcionalidad encargada de registrar al usuario"""

	def post_register(self):

		jsonfile = request.get_json()
		username = jsonfile.get('username')
		email = jsonfile.get('email')
		
		query = select([User]).where(User.email == email)
		result = db.session.execute(query)
		user = result.fetchone()

		if user == None:

			password = str( jsonfile.get('password') ).encode('utf-8')
			hash_password = bcrypt.hashpw( password, bcrypt.gensalt('10') )

			user = User(username = username, email = email, password = hash_password)
			db.session.add(user)
			db.session.commit()

			encoded = jwt.encode(jsonfile, config.KEY, algorithm = 'HS256')

			responds = {
				"status": 201,
				"message": "Successfully registered",
				"auth_token": encoded.decode("utf-8")
			}
			return responds, responds['status']

		else:
			responds = {
				"status": 400,
				"message": "There's already a user with that email"
			}
			return responds, responds['status']
			