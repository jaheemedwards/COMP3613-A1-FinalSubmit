from App.database import db

class Company(db.Model):
    companyID = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    industry = db.Column(db.String(120), nullable=False)

    def __init__(self, companyName, location, industry):
        self.companyName = companyName
        self.location = location
        self.industry = industry

    def get_json(self):
        return {
            'companyID': self.companyID,
            'companyName': self.companyName,
            'location': self.location,
            'industry': self.industry
        }
