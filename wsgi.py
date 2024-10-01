import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.controllers.controllers import add_applicant
from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )

import random
from App.models import Person
from App.models import Applicant
from App.models import Admin
from App.models import Company
from App.models import Job
from App.models import Application
from App.controllers import *

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    initialize2()
    print('database intialized')

'''
User Commands
'''

'''
# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


#Test Commands


test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

'''

'''
Hire Hub Commands
'''

hirehub = AppGroup('hirehub', help="Utilizes different features of the HireHub")

@hirehub.command('all_tables')
def display_all_tables_command():
    """Display all tables and their data."""
    display_all_tables()

@hirehub.command("add_applicant")
@click.argument("first_name")  
@click.argument("last_name") 
@click.argument("email")
@click.argument("username")
@click.argument("password")
@click.argument("resume")
def add_applicant_command(first_name, last_name, email, username, password, resume):
    """Add an applicant to the database."""
    add_applicant(first_name, last_name, email, username, password, resume)

@hirehub.command("add_company")
@click.argument("company_name")
@click.argument("location")
@click.argument("industry")
def add_company_command(company_name, location, industry):
    """Add a company to the database."""
    add_company(company_name, location, industry)

@hirehub.command("add_job")
@click.argument("title")
@click.argument("companyid")
@click.argument("salaryrange")
@click.argument("description")
@click.argument("applicationdeadline")
def add_job_command(title, companyid, salaryrange, description, applicationdeadline):
    """Add a job to the database."""
    add_job(title, companyid, salaryrange, description, applicationdeadline)

@hirehub.command("add_application")
@click.argument("applicantid")
@click.argument("jobid")
@click.argument("applicationdate")
def add_application_command(applicantid, jobid, applicationdate):
    """Add an application to the database."""
    add_application(applicantid, jobid, applicationdate)

@hirehub.command("view_applicants")
def view_applicants_command():
    """Display all applicants in the database."""
    view_applicants()

@hirehub.command("view_companies")
def view_companies_command():
    """Display all companies in the database."""
    view_companies()

@hirehub.command("view_applications")
def view_applications_command():
    """Display all applications in the database."""
    view_applications()

@hirehub.command("view_jobs")
def view_jobs_command():
    """Display all jobs in the database."""
    view_jobs()

@hirehub.command("view_applicants")
@click.argument("job_id")
def view_applicants_command(job_id):
    """View all applicants for a specific job."""
    view_job_applicants(job_id)


app.cli.add_command(hirehub)


def initialize2():
    
    add_company("BrightTech", "San Francisco", "Technology")
    add_company("InnovateLLC", "Austin", "Consulting")
    add_company("FutureNet", "Boston", "Telecommunications")
    add_company("DataWorks", "Chicago", "Data Analytics")
    add_company("GreenEnergy", "Seattle", "Renewable Energy")
    add_company("MediCare", "Los Angeles", "Healthcare")
    add_company("SkylineDevelopers", "New York", "Real Estate")
    add_company("FoodFusion", "Houston", "Food & Beverage")
    add_company("AutoMotive Solutions", "Detroit", "Automotive Manufacturing")
    add_company("FinTech Innovations", "Miami", "Financial Technology")

    # Adding 10 different jobs
    add_job("Software Engineer", 1, "$80,000 - $100,000", "Develop and maintain software applications.", "2024-12-31")
    add_job("Data Scientist", 2, "$90,000 - $120,000", "Analyze complex data to provide business insights.", "2024-11-30")
    add_job("Product Manager", 3, "$100,000 - $130,000", "Lead product development and manage teams.", "2024-10-15")
    add_job("UX Designer", 1, "$70,000 - $90,000", "Design user experiences and improve usability.", "2024-12-01")
    add_job("Systems Administrator", 4, "$60,000 - $85,000", "Manage IT infrastructure and system performance.", "2024-11-01")
    add_job("Project Manager", 5, "$90,000 - $110,000", "Coordinate project activities and manage timelines.", "2024-10-25")
    add_job("DevOps Engineer", 2, "$85,000 - $115,000", "Implement CI/CD pipelines and manage cloud infrastructure.", "2024-12-15")
    add_job("Cybersecurity Analyst", 3, "$95,000 - $125,000", "Monitor and protect systems from security threats.", "2024-11-20")
    add_job("Marketing Specialist", 5, "$60,000 - $80,000", "Develop and execute marketing strategies.", "2024-12-10")
    add_job("Database Administrator", 4, "$75,000 - $100,000", "Ensure the performance, security, and integrity of databases.", "2024-11-05")

    applicants = [
        ("Alice", "Johnson", "alice.johnson@example.com", "alicejohnson", "password123", "alice_resume.pdf"),
        ("Bob", "Smith", "bob.smith@example.com", "bobsmith", "password123", "bob_resume.pdf"),
        ("Charlie", "Brown", "charlie.brown@example.com", "charliebrown", "password123", "charlie_resume.pdf"),
        ("David", "Wilson", "david.wilson@example.com", "davidwilson", "password123", "david_resume.pdf"),
        ("Emma", "Davis", "emma.davis@example.com", "emmadavis", "password123", "emma_resume.pdf"),
        ("Frank", "Garcia", "frank.garcia@example.com", "frankgarcia", "password123", "frank_resume.pdf"),
        ("Grace", "Martinez", "grace.martinez@example.com", "gracemartinez", "password123", "grace_resume.pdf"),
        ("Henry", "Hernandez", "henry.hernandez@example.com", "henryhernandez", "password123", "henry_resume.pdf"),
        ("Ivy", "Clark", "ivy.clark@example.com", "ivyclark", "password123", "ivy_resume.pdf"),
        ("Jack", "Lopez", "jack.lopez@example.com", "jacklopez", "password123", "jack_resume.pdf"),
    ]

    for applicant in applicants:
        add_applicant(*applicant)

    # Adding applications
    application_1 = add_application(applicantID=1, jobID=1, applicationDate="2024-09-01")
    application_2 = add_application(applicantID=2, jobID=1, applicationDate="2024-09-02")
    application_3 = add_application(applicantID=1, jobID=2, applicationDate="2024-09-03")
    application_4 = add_application(applicantID=3, jobID=2, applicationDate="2024-09-04")
    application_5 = add_application(applicantID=4, jobID=3, applicationDate="2024-09-05")
    application_6 = add_application(applicantID=2, jobID=3, applicationDate="2024-09-06")
    application_7 = add_application(applicantID=5, jobID=4, applicationDate="2024-09-07")
    application_8 = add_application(applicantID=1, jobID=4, applicationDate="2024-09-08")
    application_9 = add_application(applicantID=3, jobID=5, applicationDate="2024-09-09")
    application_10 = add_application(applicantID=4, jobID=5, applicationDate="2024-09-10")