# Movie Management Web Application

## Project Summary
This project is a Flask-based web application that allows users to manage movies. It integrates with both a relational database (MySQL on AWS RDS) and a non-relational database (AWS DynamoDB).

## Technologies Used
- Flask
- MySQL (AWS RDS)
- DynamoDB (AWS)
- HTML (for templates)

## Setup and Run Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure `creds.py` with your RDS credentials.
4. Run the application: `python flaskapp.py`
5. Access the application in your browser at `http://127.0.0.1:5000`.

## Screenshots
![Screenshot of my working web app](./"C:\Users\lynne\OneDrive\CS178\Projectone\webapp.png")

## Challenges
I faced challenges of trying to use nohup to connect to my web app so that it can run without terminal interaction.

## Proposed Grade
90/100

Criteria
Points
Website uses Flask and runs independently from VS Code (not relying on terminal interaction)
10 - i had issues getting the website to run independently.

Relational database (MySQL/RDS) is correctly used in the project
15 -  i used my RDS correctly in the project

Non-relational database (DynamoDB) is correctly used (e.g., user info stored/retrieved)
10 - i used Dynamodb correctly

Implements full CRUD operations (Create, Read, Update, Delete)
10 - fully implemented CRUD

Incorporates at least one SQL JOIN query
5 - implemented a join query

Uses own RDS instance inside student’s VPC
5 - i used my own RDS instance

Uses own IAM account (e.g., ProjectOneUser)
5 - I Used my own IAM account

Application avoids storing credentials in public GitHub (e.g., creds.py is excluded via .gitignore)
5 - stored private information in creds and excluded it via gitignore


Part 2: Code Quality and GitHub Submission (25 points)
Criteria
Points
Code is organized across multiple files (e.g., flaskapp.py, dbCode.py)
10 - my code is organized across multiple files

Good software practices (clear naming, comments, error handling with try/except, modular functions)
10 - variables are clearly named and error handling is incorporated.

GitHub repository is submitted with a clear commit history and a README file
5 - Git hub repository is submitted


Part 3: Checkpoint Completion (10 points)
Criteria
Points
Checkpoint submitted on time with a working Flask app that connects to RDS and renders dynamic data
10

