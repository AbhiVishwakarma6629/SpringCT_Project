# SpringCT_Project# Flask API with Authentication & Role-Based Access Control (RBAC)

This project is a Flask-based RESTful API with PostgreSQL as the database. It includes authentication using JWT, user roles (Admin & Customer), and secure endpoints. Admins can manage products, orders, and users, while customers can view products and place orders.

## Features
- User authentication with JWT (Login, Logout, Token Refresh)
- Role-Based Access Control (RBAC) for Admin and Customer users
- Secure password hashing
- CRUD operations for products and orders
- API request rate-limiting
- Caching for product listing

## Installation Guide

### 1. Clone the Repository
```sh
git clone https://github.com/AbhiVishwakarma6629/SpringCT_Project.git
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database
1. Open PostgreSQL terminal (psql) and run:
```sql
CREATE DATABASE ecom;
```
2. Update the `.env` file with database credentials:
```
DATABASE_URL=postgresql://ecom_user:password@localhost/ecom
SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_here
```

### 5. Run Migrations
```sh
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 6. Run the Flask Application
```sh
flask run
```

### 7. Testing the API
Use Postman or any API client to test the endpoints.

## API Endpoints

### Authentication
- **POST /auth/login** → Authenticate user and return JWT token.
- **GET /auth/logout** → Invalidate JWT token.

### Products (Admin Only)
- **GET /products** → List products (available to customers too)
- **GET /products/{id}** → Get product details
- **POST /products** → Add a new product (Admin only)
- **PUT /products/{id}** → Update a product (Admin only)
- **DELETE /products/{id}** → Delete a product (Admin only)

### Orders (Customers & Admins)
- **GET /orders** → View all orders (Admins can filter by status and user_id)
- **POST /orders** → Place a new order (Customers only)
- **GET /orders/{id}** → View order details
- **DELETE /orders/{id}** → Cancel an order (Admin only)

### Security Measures
- Password hashing using Flask-Bcrypt
- JWT authentication with refresh tokens
- Role-based access control (RBAC)
- Rate limiting (100 requests per minute per user)
- Caching (Product list cached for 5 minutes)