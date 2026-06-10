E-Commerce Backend API

Intern Information

- Intern ID: CITS1859
- Full Name: Snehal Bhandarkar
- No. of Weeks: 4 Weeks

Project Name

E-Commerce Backend API using FastAPI

Project Description

An advanced E-Commerce Backend API developed using FastAPI. The system provides user registration, product management, and RESTful API endpoints for managing e-commerce operations efficiently.

Project Scope

The project is designed to demonstrate backend development concepts including API creation, database integration, data validation, and CRUD operations using FastAPI and SQLite.

Features

- User Registration
- Product Management
- RESTful API Endpoints
- SQLite Database Integration
- Swagger API Documentation
- Fast and Lightweight Backend

Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- VS Code

Project Structure

Ecommerce-Backend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
├── screenshots/
└── documentation/

Installation

Install dependencies:

pip install -r requirements.txt

Run the Project

uvicorn main:app --reload

API Documentation

Open:

http://127.0.0.1:8000/docs

Available APIs

User APIs

- POST /register

Product APIs

- POST /products
- GET /products

Output

The API allows users to register, add products, and retrieve product information through REST endpoints.

Screenshots Included

- Swagger UI Home Page
- User Registration API
- Product Creation API
- Product Listing API

Conclusion

This project demonstrates the implementation of a scalable backend system using FastAPI and SQLite. It provides a foundation for developing full-featured e-commerce applications.