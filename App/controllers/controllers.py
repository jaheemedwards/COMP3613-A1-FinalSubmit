from App.models import db, Applicant, Admin, Company, Job, Application

def add_company(companyName, location, industry):
    newCompany = Company(companyName=companyName, location=location, industry=industry)
    db.session.add(newCompany)
    db.session.commit()

    print(f"Company '{companyName}' has been added successfully.")
    return newCompany

def add_job(title, companyID, salaryRange, description, applicationDeadline):
    # Create a new Job object
    new_job = Job(
        title=title, 
        companyID=companyID, 
        salaryRange=salaryRange, 
        description=description, 
        applicationDeadline=applicationDeadline
    )
    
    db.session.add(new_job)
    db.session.commit()
    
    print(f"Job '{title}' has been added successfully.")
    return new_job

def add_applicant(firstName, lastName, email, username, password, resume):
    newApplicant = Applicant(firstName=firstName, lastName=lastName, email=email, username=username, password=password, resume=resume)
    try:
        db.session.add(newApplicant)
        db.session.commit()
        print(f"Successfully added applicant {firstName} {lastName}.")
        return newApplicant
    except Exception as e:
        db.session.rollback()
        print(f"Failed to add applicant {firstName} {lastName}. Error: {e}")
        return None

def add_admin(firstName, lastName, email, username, password, companyID):
    newAdmin = Admin(firstName=firstName, lastName=lastName, email=email, username=username, password=password, companyID=companyID)
    try:
        db.session.add(newAdmin)
        db.session.commit()
        print(f"Successfully added admin {firstName} {lastName}.")
        return newAdmin
    except Exception as e:
        db.session.rollback() 
        print(f"Failed to add admin {firstName} {lastName}. Error: {e}")
        return None

def add_application(applicantID, jobID, applicationDate):
    newApplication = Application(applicantID=applicantID, jobID=jobID, applicationDate=applicationDate)
    try:
        db.session.add(newApplication)
        db.session.commit()
        print(f"Successfully added application for applicant ID {applicantID} to job ID {jobID}.")
        return newApplication
    except Exception as e:
        db.session.rollback() 
        print(f"Failed to add application for applicant ID {applicantID} to job ID {jobID}. Error: {e}")
        return None

def display_all_tables():
    # Display all companies
    companies = Company.query.all()
    print("Companies:")
    for company in companies:
        print(company.__dict__)
    print("\n")

    # Display all applicants
    applicants = Applicant.query.all()
    print("Applicants:")
    for applicant in applicants:
        print(applicant.get_json())
    print("\n")

    # Display all admins
    admins = Admin.query.all()
    print("Admins:")
    for admin in admins:
        print(admin.get_json())
    print("\n")

    # Display all jobs
    jobs = Job.query.all()
    print("Jobs:")
    for job in jobs:
        print(job.__dict__)
    print("\n")

    # Display all applications
    applications = Application.query.all()
    print("Applications:")
    for application in applications:
        print(application.__dict__) 
    print("\n")

def view_jobs():
    try:
        jobs = Job.query.all()
        if not jobs:
            print("No jobs found.")
            return
        
        for job in jobs:
            print(f"Job ID: {job.id}, Title: {job.title}, Company ID: {job.companyID}, "
                  f"Salary Range: {job.salaryRange}, Description: {job.description}, "
                  f"Application Deadline: {job.applicationDeadline}")
    except Exception as e:
        print(f"An error occurred while retrieving jobs: {e}")

def view_applicants():
    try:
        applicants = Applicant.query.all()  
        if not applicants:
            print("No applicants found.")
            return
        
        for applicant in applicants:
            print(f"Applicant ID: {applicant.id}, Name: {applicant.firstName} {applicant.lastName}, "
                  f"Email: {applicant.email}, Username: {applicant.username}")
    except Exception as e:
        print(f"An error occurred while retrieving applicants: {e}")

def view_companies():
    try:
        companies = Company.query.all() 
        if not companies:
            print("No companies found.")
            return
        
        for company in companies:
            print(f"Company ID: {company.companyID}, Name: {company.companyName}, "
                  f"Location: {company.location}, Industry: {company.industry}")
    except Exception as e:
        print(f"An error occurred while retrieving companies: {e}")

def view_applications():
    try:
        applications = Application.query.all()
        if not applications:
            print("No applications found.")
            return
        
        for application in applications:
            print(f"Application ID: {application.applicationID}, Applicant ID: {application.applicantID}, "
                  f"Job ID: {application.jobID}, Application Date: {application.applicationDate}")
    except Exception as e:
        print(f"An error occurred while retrieving applications: {e}")

def view_job_applicants(job_id):
    try:
        applications = Application.query.filter_by(jobID=job_id).all()
        
        if not applications:
            print(f"No applicants found for Job ID: {job_id}.")
            return
        
        print(f"Applicants for Job ID: {job_id}:")
        for application in applications:
            applicant = Applicant.query.get(application.applicantID)  # Retrieve applicant details
            print(f"Applicant ID: {applicant.id}, Name: {applicant.firstName} {applicant.lastName}, Email: {applicant.email}")
    except Exception as e:
        print(f"An error occurred while retrieving applicants for Job ID {job_id}: {e}")
