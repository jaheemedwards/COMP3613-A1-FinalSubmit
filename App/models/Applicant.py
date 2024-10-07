from App.database import db
from .Person import Person
from .Job import *
from .Application import *

class Applicant(Person):
    resume = db.Column(db.String(20), nullable=True)
    applications = db.relationship('Application', backref='applicant', lazy=True)

    def __init__(self, firstName, lastName, email, username, password, resume):
        super().__init__(firstName=firstName, lastName=lastName, email=email, username=username, password=password)
        self.resume = resume

    def get_json(self):
        person_data = super().get_json()
        person_data['resume'] = self.resume
        return person_data

    def applyToJob(self, jobID: int, applicationDate: str) -> bool:
        """Apply to a job by creating a new application."""
        job = Job.query.get(jobID)
        if not job:
            print(f"Job with ID {jobID} does not exist.")
            return False

        application = Application(applicantID=self.id, jobID=jobID, applicationDate=applicationDate)
        db.session.add(application)
        db.session.commit()
        print(f"Application submitted for Job ID {jobID}.")
        return True

    def viewApplication(self, applicationID: int) -> bool:
        """View a specific application by its ID."""
        application = Application.query.filter_by(applicantID=self.id, applicationID=applicationID).first()
        if application:
            print(application.get_json())
            return True
        else:
            print(f"No application found with ID {applicationID} for applicant ID {self.id}.")
            return False

    def updateApplication(self, applicationID: int, newApplicationDate: str) -> bool:
        """Update the application date of an existing application."""
        application = Application.query.filter_by(applicantID=self.id, applicationID=applicationID).first()
        if application:
            application.applicationDate = newApplicationDate
            db.session.commit()
            print(f"Application ID {applicationID} updated successfully.")
            return True
        else:
            print(f"Application ID {applicationID} not found for applicant ID {self.id}.")
            return False