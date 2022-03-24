from src import db
from src.constants import TXN_TABLE_NAME, STATUS_TRUE, STATUS_FALSE, USER_FOREIGN_KEY


class Transactions(db.Model):
    __tablename__ = TXN_TABLE_NAME
    transaction_id = db.Column(db.String(50), primary_key=STATUS_TRUE, nullable=STATUS_FALSE)
    mobile_number = db.Column(db.String(50), unique=STATUS_TRUE, nullable=STATUS_FALSE)
    transaction_date = db.Column(db.DateTime(), nullable=STATUS_FALSE)


db.create_all()
