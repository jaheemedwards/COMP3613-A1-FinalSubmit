# COMP3613-A1-FinalSubmit

# Hire Hub CLI Commands

The Hire Hub application provides a command-line interface (CLI) to manage job applicants, companies, jobs, and applications. Below are the available commands you can use:

## Commands

### 1. Display All Tables

```bash
flask hirehub all_tables
```
- **Description:** Display all tables and their data.

### 2. Add Applicant

```bash
flask hirehub add_applicant <first_name> <last_name> <email> <username> <password> <resume>
```
- **Description:** Add an applicant to the database.
- **Arguments:**
  - `first_name`: The applicant's first name.
  - `last_name`: The applicant's last name.
  - `email`: The applicant's email address.
  - `username`: The applicant's username.
  - `password`: The applicant's password.
  - `resume`: The filename of the applicant's resume.

### 3. Add Company

```bash
flask hirehub add_company <company_name> <location> <industry>
```
- **Description:** Add a company to the database.
- **Arguments:**
  - `company_name`: The name of the company.
  - `location`: The company's location.
  - `industry`: The industry in which the company operates.

### 4. Add Job

```bash
flask hirehub add_job <title> <companyid> <salaryrange> <description> <applicationdeadline>
```
- **Description:** Add a job to the database.
- **Arguments:**
  - `title`: The title of the job.
  - `companyid`: The ID of the company offering the job.
  - `salaryrange`: The salary range for the job (e.g., "50000-70000").
  - `description`: A description of the job.
  - `applicationdeadline`: The deadline for applications (e.g., "2024-12-31").

### 5. Add Application

```bash
flask hirehub add_application <applicantid> <jobid> <applicationdate>
```
- **Description:** Add an application to the database.
- **Arguments:**
  - `applicantid`: The ID of the applicant.
  - `jobid`: The ID of the job.
  - `applicationdate`: The date of the application (e.g., "2024-09-30").

### 6. View All Applicants

```bash
flask hirehub view_applicants
```
- **Description:** Display all applicants in the database.

### 7. View All Companies

```bash
flask hirehub view_companies
```
- **Description:** Display all companies in the database.

### 8. View All Applications

```bash
flask hirehub view_applications
```
- **Description:** Display all applications in the database.

### 9. View All Jobs

```bash
flask hirehub view_jobs
```
- **Description:** Display all jobs in the database.

### 10. View Applicants for a Job

```bash
flask hirehub view_applicants <job_id>
```
- **Description:** View all applicants for a specific job.
- **Arguments:**
  - `job_id`: The ID of the job for which to view applicants.

## Usage Example

To add an applicant, you would run:

```bash
flask hirehub add_applicant "John" "Doe" "john.doe@example.com" "johndoe" "password123" "resume.pdf"
```

This command adds a new applicant with the provided details to the database.
```

This section clearly outlines the available CLI commands, their descriptions, and usage examples. You can integrate this into your existing `README.md` or create a new one focused solely on CLI usage.
