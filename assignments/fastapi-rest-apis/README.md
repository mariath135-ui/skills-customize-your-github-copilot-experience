# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, students will learn to build RESTful APIs using the FastAPI framework in Python. They will create endpoints, handle path parameters, and process request bodies.

## 📝 Tasks

### 🛠️	Task 1: Set Up a Basic FastAPI Application

#### Description
Create a new FastAPI application with a simple GET endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at "/" that returns a JSON response with a "message" key
- Include proper type hints and docstrings


### 🛠️	Task 2: Add Dynamic Endpoints

#### Description
Extend the API by adding endpoints that use path parameters and handle POST requests with JSON data.

#### Requirements
Completed program should:

- Add a GET endpoint with a path parameter (e.g., /items/{item_id}) that returns item details
- Add a POST endpoint to create new items, accepting JSON data in the request body
- Use Pydantic models for request and response validation
- Handle basic error cases (e.g., item not found)