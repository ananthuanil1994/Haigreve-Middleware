from src import db
from src.constants import TXN_TABLE_NAME, STATUS_TRUE, STATUS_FALSE


class Transactions(db.Model):
    __tablename__ = TXN_TABLE_NAME
    transaction_id = db.Column(db.String(50),  primary_key=STATUS_TRUE, nullable=STATUS_FALSE)
    mobile_number = db.Column(db.String(50), unique=STATUS_FALSE, nullable=STATUS_FALSE)
    time = db.Column(db.String(20), nullable=STATUS_FALSE)
    short_code = db.Column(db.String(50), nullable=STATUS_FALSE)
    text = db.Column(db.String(20), nullable=STATUS_FALSE)
    mnocode = db.Column(db.String(20), nullable=STATUS_FALSE)
    status = db.Column(db.String(20), nullable=STATUS_FALSE)
    type = db.Column(db.String(20), nullable=STATUS_FALSE)
    service_id = db.Column(db.String(50), nullable=STATUS_FALSE)


db.create_all()
