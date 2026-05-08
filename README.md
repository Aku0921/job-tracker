#Job-Tracker App

This application helps the user track their job applications and helps organize them. The users are able to store applications, follow-up dates and also maintain notes for each application.

Purpose:
    Without proper tracking, managing multiple applications are difficult. This project simplifies the process by providing a centralized system to mainatain all applications.

Tech used: Python and FastAPI (backend)
           HTML,CSS and js (frontend)
           PostgreSQL (database)
           Git,VS Code and GitHub (tools)

Features:
    - Add new job applications
    - View all applications
    - Delete applications
    - Update applications
    - Add notes
    - Track follow-up dates
    - Filter and search applications

Project Structure:
JOBTRACKER/
|--app/
||--main.py
||--database.py
||--crud.py
||--models.py
||--schemas.py
||--routes/
|
|--frontend/
|--requirements.txt
|--README.md

Database:
Application table:
-id
-company_name
-role
-application_date
-status
-notes
-follow_up_date

Future scope:
-authentication
-email reminders
-resume upload feature
-interview scheduling

Goals:
Through this project I aim to improve:
-API development with FastAPI
-Database design with PostgreSQL
-Frontend integration with backend
-Deployment and version control
