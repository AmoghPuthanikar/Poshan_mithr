🍎 Nutrition Management System

A comprehensive school nutrition management platform built with FastAPI and SQLAlchemy to track student health, calculate BMI, detect nutritional deficiencies, and generate personalized Indian diet recommendations.

✨ Features
🧑‍⚖️ Role-Based Access Control

Admin (District CEO): Monitor district-wide nutrition analytics

Authority (Headmaster): Manage classrooms and student records

Parent: Track child’s health and dietary recommendations

👩‍🎓 Student Management

Add students with automatic parent account creation

Organize students into classrooms

Track dietary preferences (Veg / Non-Veg)

🥗 Nutrition Calculator

BMI calculation with age-appropriate percentiles

Status classification: Underweight, Healthy, Overweight, Obese

Detect common nutritional deficiencies

Generate personalized Indian diet plans

👨‍👩‍👧 Parent Portal

View child’s health dashboard

Access diet recommendations

Monitor growth and nutrition progress

🚀 Tech Stack

Backend: FastAPI (Python)

Database: SQLAlchemy with SQLite (PostgreSQL supported)

Frontend: Bootstrap 5, Jinja2 Templates

Authentication: JWT with bcrypt password hashing

📋 Prerequisites

Python 3.8+

pip (Python package manager)

⚙️ Installation

Clone the repository

git clone <your-repo-url>
cd nutrition_mvp


Create a virtual environment

python -m venv venv


Activate the virtual environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Seed the database with sample data

python -m app.seed_data


Run the application

python -m app.main


Access the web app

http://localhost:8000

🔐 Demo Login Credentials
Role	Username	Password
Admin	admin	admin123
Headmaster	head1	pass123
Parent	parent1	pass123
📂 Project Structure
nutrition_mvp/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── admin_dashboard.html
│   │   ├── authority_dashboard.html
│   │   ├── parent_dashboard.html
│   │   ├── create_kid.html
│   │   ├── create_classroom.html
│   │   ├── nutrition_calculator.html
│   │   └── nutrition_results.html
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── auth.py
│   ├── nutrition_calculator.py
│   └── seed_data.py
├── venv/
├── .gitignore
├── requirements.txt
└── README.md

🎯 Usage
👨‍🏫 Headmaster

Log in with headmaster credentials

Create classrooms and add students

Run the nutrition calculator for assessments

Generate personalized diet recommendations

👩‍👩‍👧 Parent

Log in with parent credentials

View child’s health dashboard

Monitor BMI and nutrition status

Follow suggested meal plans

🏢 Admin

Log in as admin

Access district-level analytics

Track school nutrition performance trends

🔧 Configuration
Change JWT Secret Key

Edit app/auth.py:

SECRET_KEY = "your-secret-key-here"

Switch to PostgreSQL

Edit app/database.py:

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

📊 Detailed Features
🧮 BMI Calculator

Calculates BMI percentiles by age

Classifies status: Underweight, Healthy, Overweight, Obese

Detects nutritional deficiencies (Iron, Calcium, Protein, etc.)

🍽️ Personalized Diet Plans

Vegetarian and Non-Vegetarian meal options

Traditional Indian diet plans

Status-specific nutrition advice

Meal suggestions for Breakfast, Lunch, Dinner, and Snacks

🤝 Contributing

Contributions are welcome!
Fork the repository, create a new branch, make changes, and submit a Pull Request.