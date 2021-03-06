from src import db
from src.constants import STATUS_TRUE, STATUS_FALSE, TOKEN_TABLE_NAME


class Tokens(db.Model):
    __tablename__ = TOKEN_TABLE_NAME
    id = db.Column(db.Integer, primary_key=STATUS_TRUE)
    access_token = db.Column(db.String(600), unique=STATUS_TRUE, nullable=STATUS_FALSE)
    refresh_token = db.Column(db.String(600), unique=STATUS_TRUE, nullable=STATUS_FALSE)


db.create_all()
