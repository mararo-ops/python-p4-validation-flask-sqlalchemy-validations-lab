from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import UniqueConstraint, CheckConstraint
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String,CheckConstraint('length(phone_number) = 10'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

   # Custom validation for name
    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name is required.")
        return value
#custom validation for phone number
    @validates('phone_number')
    def validate_number(self,key,phone_number):
      if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValueError("Phone number must be exactly ten digits.")
      return phone_number
  
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String,CheckConstraint('length(content) >= 250'))
    category = db.Column(db.String,CheckConstraint('category IN ("Fiction", "Non-Fiction")'))
    summary = db.Column(db.String,CheckConstraint('length(summary) <= 250'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self,key,title):
        if "Won't Believe" and "Secret" and "Top [number]" and "Guess" not in title:
            raise ValueError('ERROR')
        return title
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'