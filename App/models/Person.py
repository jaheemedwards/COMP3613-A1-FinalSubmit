from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .Job import *

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, firstName, lastName, email, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.set_password(password)

    def get_json(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def login(self, password: str) -> bool:
        """Check if the password is correct for login."""
        if self.check_password(password):
            print(f"{self.username} logged in successfully.")
            return True
        else:
            print(f"Login failed for {self.username}.")
            return False

    def logout(self) -> bool:
        """Simulate logout."""
        print(f"{self.username} logged out successfully.")
        return True

    def viewJobs(self) -> None:
        """Display all available jobs."""
        jobs = Job.query.all()
        if jobs:
            for job in jobs:
                print(job.get_json())
        else:
            print("No jobs available.")