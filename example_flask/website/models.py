from website import db
import random

# One-to-Many Relationship
# http://flask-sqlalchemy.pocoo.org/2.3/models/#one-to-many-relationships


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)


# Many-to-Many Relationship
# http://flask-sqlalchemy.pocoo.org/2.3/models/#many-to-many-relationships


tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
                )


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('pages', lazy=True))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# custom helper
class Queries:

    @staticmethod
    def random(o: db.Model, i: int):
        """ returns random :param i: rows for :param o: object """
        c = o.query.count()
        if c <= 1:
            return o.query.all()
        x = random.sample(range(1, int()), i)
        return o.query.filter(o.id.in_(x)).all()
