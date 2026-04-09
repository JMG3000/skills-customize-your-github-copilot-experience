# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a simple REST API with FastAPI that can create, read, update, and delete course resources using Python functions, request data, and JSON responses.

## 📝 Tasks

### 🛠️ FastAPI App Setup

#### Description
Create a FastAPI application with a root endpoint and a small in-memory data store for sample records.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Define a root endpoint that returns a welcome message.
- Store sample data in memory using a Python list or dictionary.
- Return JSON responses from endpoints.

### 🛠️ CRUD Endpoints

#### Description
Add endpoints that let users create, view, update, and delete records through the API.

#### Requirements
Completed program should:

- Create a `GET` endpoint to list all records.
- Create a `GET` endpoint to retrieve one record by ID.
- Create a `POST` endpoint to add a new record.
- Create a `PUT` or `PATCH` endpoint to update an existing record.
- Create a `DELETE` endpoint to remove a record.
- Handle missing records with a clear error response.
