from App.database import db
from .Company import *

class Job(db.Model):
    jobID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    companyID = db.Column(db.Integer, db.ForeignKey('company.companyID'), nullable=False)
    company = db.relationship('Company', backref='jobs', lazy=True)
    salaryRange = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    applicationDeadline = db.Column(db.String(120), nullable=False)

    def __init__(self, title, companyID, salaryRange, description, applicationDeadline):
        self.title = title
        self.companyID = companyID
        self.salaryRange = salaryRange
        self.description = description
        self.applicationDeadline = applicationDeadline

    def get_json(self):
        return {
            'jobID': self.jobID,
            'title': self.title,
            'companyID': self.companyID,
            'salaryRange': self.salaryRange,
            'description': self.description,
            'applicationDeadline': self.applicationDeadline
        }

    @staticmethod
    def createJob(title: str, salaryRange: str, description: str, applicationDeadline: str, companyID: int) -> bool:
        """Create a new job posting."""
        company = Company.query.get(companyID)
        if not company:
            print(f"Company with ID {companyID} does not exist.")
            return False

        new_job = Job(title=title, salaryRange=salaryRange, description=description, applicationDeadline=applicationDeadline, companyID=companyID)
        db.session.add(new_job)
        db.session.commit()
        print(f"Job '{title}' created successfully.")
        return True

    @staticmethod
    def updateJob(jobID: int, title: str = None, salaryRange: str = None, description: str = None, applicationDeadline: str = None) -> bool:
        """Update an existing job posting."""
        job = Job.query.get(jobID)
        if not job:
            print(f"Job with ID {jobID} does not exist.")
            return False

        if title:
            job.title = title
        if salaryRange:
            job.salaryRange = salaryRange
        if description:
            job.description = description
        if applicationDeadline:
            job.applicationDeadline = applicationDeadline

        db.session.commit()
        print(f"Job ID {jobID} updated successfully.")
        return True

    @staticmethod
    def deleteJob(jobID: int) -> bool:
        """Delete an existing job posting."""
        job = Job.query.get(jobID)
        if not job:
            print(f"Job with ID {jobID} does not exist.")
            return False

        db.session.delete(job)
        db.session.commit()
        print(f"Job ID {jobID} deleted successfully.")
        return True