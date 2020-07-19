from app.models import db

class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	title = db.Column(db.String(255), nullable = False)
	imdb_id = db.Column(db.Integer, nullable = False)
	year = db.Column(db.Integer, nullable = False)
	runtime = db.Column(db.String(255), nullable = False)
	genre = db.Column(db.String(255), nullable = False)
	director = db.Column(db.String(255), nullable = False)
	actors = db.Column(db.String(255), nullable = False)
	synopsis = db.Column(db.Text, nullable = False)
	imdb_rating = db.Column(db.Float(), nullable = False)