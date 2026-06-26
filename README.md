# 🛍️ Product Catalog REST API

A simple RESTful API built with Python and Flask that exposes
a fictional product catalog with filtering and dynamic routing.

---

## 🚀 Getting Started

### Install dependencies
pip install -r requirements.txt

### Run the server
python app.py

Server runs at: http://127.0.0.1:5000

---

## 📡 Endpoints

| Method | Route                          | Description                     |
|--------|--------------------------------|---------------------------------|
| GET    | `/`                            | Welcome message + route index   |
| GET    | `/products`                    | Return all products             |
| GET    | `/products?category=books`     | Filter products by category     |
| GET    | `/products/<id>`               | Return a single product by ID   |

---

## 🧪 Usage Examples

### 1. Homepage
GET http://127.0.0.1:5000/

**Response:**
{
  "message": "Welcome to the Product Catalog API!",
  "version": "1.0.0",
  "endpoints": { ... }
}

---

### 2. All Products
GET http://127.0.0.1:5000/products

**Response:**
{
  "count": 8,
  "products": [ { "id": 1, "name": "The Great Gatsby", ... }, ... ]
}

---

### 3. Filter by Category
GET http://127.0.0.1:5000/products?category=electronics

**Response:**
{
  "category": "electronics",
  "count": 2,
  "products": [ { "id": 3, "name": "Wireless Headphones", ... }, ... ]
}

---

### 4. Single Product by ID
GET http://127.0.0.1:5000/products/1

**Response:**
{
  "product": { "id": 1, "name": "The Great Gatsby", "category": "books", "price": 10.99 }
}

---

### 5. Product Not Found (404)
GET http://127.0.0.1:5000/products/999

**Response (404):**
{
  "error": "Product not found",
  "product_id": 999
}

---

## 📂 Project Structure
flask-product-api/
├── app.py              # Main Flask application
├── data/
│   └── products.py     # Mock product dataset
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

---

## ✅ Design Decisions
- Plural nouns used in all routes (/products)
- All categories normalized to lowercase for consistent filtering
- 404 errors return JSON (not HTML) for API consistency
- Status codes: 200 OK, 404 Not Found used appropriately