from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Usuario(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    apellido = db.Column(db.String(120), unique=False, nullable=False)
    email  = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    usuario_favoritos = relationship('Favorito', backref='usuario', lazy=True)

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "password": self.password,
            "usuario_favoritos": list(map(lambda item: item.serialize(),self.usuario_favoritos))
            # do not serialize the password, its a security breach
        }


class Personajes(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    mass = db.Column(db.String(120), unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "mass" : self.mass,
            "hair_color" : self.hair_color,
            "skin_color" : self.skin_color,
            "eye_color" : self.eye_color,
            "birth_year" : self.birth_year,
            "gender" : self.gender,
            "height" : self.height
            # do not serialize the password, its a security breach
        }


class Planetas(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120), unique=False, nullable=False)
    rotation_period = db.Column(db.String(120), unique=False, nullable=False)
    orbital_period = db.Column(db.String(120), unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
            # do not serialize the password, its a security breach
        }


class Vehiculos(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=True, nullable=False)
    vehicle_class = db.Column(db.String(120), unique=False, nullable=False)
    manufacturer = db.Column(db.String(120), unique=False, nullable=False)
    cost_in_credits = db.Column(db.String(120), unique=False, nullable=False)
    length = db.Column(db.String(120), unique=False, nullable=False)
    crew = db.Column(db.String(120), unique=False, nullable=False)
    passengers = db.Column(db.String(120), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.String(120), unique=False, nullable=False)
    cargo_capacity = db.Column(db.String(120), unique=False, nullable=False)
    consumables = db.Column(db.String(120), unique=False, nullable=False)
    films = db.Column(db.String(120), unique=False, nullable=False)
    pilots = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "model" : self.model,
            "vehicle_class" : self.vehicle_class,
            "manufacturer" : self.manufacturer,
            "cost_in_credits" : self.cost_in_credits,
            "length" : self.length,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "cargo_capacity" : self.cargo_capacity,
            "consumables" : self.consumables,
            "films" : self.films,
            "pilots" : self.pilots,
            # do not serialize the password, its a security breach
        }


class Favorito(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Personajes)

    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    vehiculos = relationship(Vehiculos)

    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Planetas)

    def __repr__(self):
        return '<Favorito %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            # "usuario" : self.usuario,
            "personaje": None if self.personajes is None else self.personajes.serialize(),
            # "personajes" : self.personajes,
            "vehiculo": None if self.vehiculos is None else self.vehiculos.serialize(),
            # "vehiculos" : self.vehiculos,
            "planeta": None if self.planetas is None else self.planetas.serialize(),
            # "planetas" : self.planetas,
            # do not serialize the password, its a security breach
        }
