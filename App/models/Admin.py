from App.database import db
from .Person import *
from .Company import *
from .Application import *
from .Job import *

class Admin(Person):
    companyID = db.Column(db.Integer, db.ForeignKey('company.companyID'), nullable=True)
    
    def __init__(self, firstName, lastName, email, username, password, companyID):
        super().__init__(firstName, lastName, email, username, password)
        self.companyID = companyID

    def get_json(self):
        person_data = super().get_json()
        person_data['companyID'] = self.companyID
        return person_data
    
    def createJob(self, title, salaryRange, description, applicationDeadline):
        """Create a job by calling Job's createJob method"""
        new_job = Job(title, salaryRange, description, applicationDeadline)
        return new_job.createJob()

    def updateJob(self, jobID, new_title, new_salaryRange, new_description, new_applicationDeadline):
        """Update a job by calling Job's updateJob method"""
        job = Job.query.get(jobID)
        if job:
            return job.updateJob(new_title, new_salaryRange, new_description, new_applicationDeadline)
        return False

    def deleteJob(self, jobID):
        """Delete a job by calling Job's deleteJob method"""
        job = Job.query.get(jobID)
        if job:
            return job.deleteJob()
        return False
