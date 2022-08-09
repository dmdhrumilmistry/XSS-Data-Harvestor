from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HackedData(db.Model):
    __tablename__ = 'hackedData'

    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    ip = db.Column('ip', db.String(50), nullable=False)
    data = db.Column('data', db.String(500), nullable=False)

    def __init__(self, ip: str, data: str):
        self.ip = ip
        self.data = data

    def __str__(self) -> str:
        return f'{self.id}-{self.ip}-{self.data}'
