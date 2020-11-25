from sqlalchemy.sql import Select, expression

from app.loader import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    is_superuser = db.Column(db.Boolean, server_default=expression.false())
    query: Select
