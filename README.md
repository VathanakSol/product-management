# Product Management System Console App

A simple Python console application demonstrating object-oriented design for product management.

The app is organized into clear layers to separate concerns and make the system easy to extend:

## Using OOP Python

- Model: defines product data structures and shared behavior.
- Repository: manages product storage and persistence logic.
- Service: contains application business rules and product operations.
- View (main.py): serves as the program entry point and user interaction layer.

## Structure of Project

### Model
- Defines the product schema and base behavior.
- Includes `base.py` and `product.py`.

### Repository
- Stores and retrieves product data.
- Implements `ProductRepository` in `repository/product.py`.

### Service
- Controls application logic for product operations.
- Implements `ProductService` in `service/product.py`.

### View
- `main.py` is the entry point that runs the console app.
- Coordinates input/output and uses the service layer.

This project is useful for learning how to structure a small Python application using OOP principles and layered architecture.
