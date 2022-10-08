from app import db
# import flask_login


# User database

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # crops = db.relationship('Crops', back_populates='users')


# Sow table


class Crops(db.Model):
    crop_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crop_name = db.Column(db.String, nullable=False)
    sow_date = db.Column(db.Date, nullable=False)
    # users = db.relationship('Users', back_populates='users')
    # harvests = db.relationship('Harvests', back_populates='harvests')

# Harvest Table


class Harvests(db.Model):
    harvest_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    harvest_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    units = db.Column(db.String, nullable=False)
    # harvests = db.relationship('Crops', back_populates='crops')


# sow_harvest_users_table = db.Table(
#     'crops', id,
#     db.Column('user_id', db.Integer, db.ForeignKey('Users.id')),
#     db.Column('crop-id', db.Integer, db.ForeignKey('Crop.id')),
#     db.Column('harvest-id', db.Integer, db.ForeignKey('Harvest.id'))
# )
