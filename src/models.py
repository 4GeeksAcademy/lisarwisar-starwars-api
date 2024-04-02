from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

class Characters(db.Model):
    __tablename__ = "characters"
    name = db.Column(db.String(250), primary_key=True)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)

class Planets(db.Model):
    __tablename__ = "planets"
    name = db.Column(db.String(250), primary_key=True)
    diameter = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    residents = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)

class Items(db.Model):
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)

class Favorite_Characters(db.Model):
    __tablename__ = "favorite_characters"
    user_character_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    character_name = db.Column(db.String(250), db.ForeignKey("characters.name"))

class Favorite_Planets(db.Model):
    __tablename__ = "favorite_planets"
    user_planer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_name = db.Column(db.String(250), db.ForeignKey("planets.name"))