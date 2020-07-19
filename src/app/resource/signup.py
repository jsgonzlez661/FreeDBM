from app.resource import *

class Signup(Resource):

	def post(self):
		jsonfile = request.get_json()
		username = jsonfile.get('username')
		email = jsonfile.get('email')
		
		query = select([User]).where(User.email == email)
		result = db.session.execute(query)
		user = result.fetchone()

		if user == None:
			password = str(jsonfile.get('password')).encode('utf-8')
			hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

			user = User(username = username, email = email, password = hash_password)
			db.session.add(user)
			db.session.commit()

			encoded = jwt.encode(jsonfile, config.KEY, algorithm = 'HS256')
			responds = {
				"status": "success",
				"message": "Successfully registered",
				"auth_token": encoded.decode("utf-8")
			}
			return responds, 201
		else:
			responds = {
				"status": "fail",
				"message": "There's already a user with that email"
			}
			return responds, 401