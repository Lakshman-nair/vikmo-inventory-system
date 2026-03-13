# 📦 Django Sales Order & Inventory Management System

A **Sales Order and Inventory Management System** built using **Django** and **Django REST Framework**.
This project allows businesses to manage **products, dealers, inventory, and sales orders** through REST APIs and a simple dashboard interface.

---

# 🚀 Features

* Product Management
* Dealer Management
* Inventory Tracking
* Sales Order Creation
* Order Item Management
* REST API using Django REST Framework
* Simple Bootstrap-based dashboard
* SKU-based product identification

---

# 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* HTML
* Bootstrap

---

# 📂 Project Structure

```
vikmo_project/
│
├── vikmo/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── inventory_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── templates/
│   │   └── inventory_app/
│   │       ├── index.html
│   │       ├── add_product.html
│   │       └── create_order.html
│
├── manage.py
└── db.sqlite3
```

---

# 📊 Database Models

## Product

* id
* name
* sku (unique)
* price

## Dealer

* id
* name
* email

## Inventory

* id
* product
* quantity

## Order

* id
* dealer
* status

## Order Item

* id
* order
* product
* quantity
* unit_price
* line_total

---

# 🔌 API Endpoints

| Endpoint         | Description       |
| ---------------- | ----------------- |
| `/products/`     | List all products |
| `/dealers/`      | List all dealers  |
| `/orders/`       | List all orders   |
| `/inventory/`    | List inventory    |
| `/add-product/`  | Add new product   |
| `/create-order/` | Create new order  |

---

# ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/sales-inventory-system.git
cd sales-inventory-system
```

---

### 2️⃣ Create Virtual Environment

Mac / Linux

```
python3 -m venv venv
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install django djangorestframework
```

---

### 4️⃣ Run Migrations

```
python3 manage.py makemigrations
python3 manage.py migrate
```

---

### 5️⃣ Run Server

```
python3 manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

# 🧮 Order Calculation Example

```
Quantity = 5
Unit Price = 800

Line Total = Quantity × Unit Price
Line Total = 4000
```

---

# 🔮 Future Improvements

* Inventory auto-update when order is placed
* Order total calculation
* Authentication system
* Product search
* Advanced dashboard analytics
* React frontend

---

# 👨‍💻 Author

Lakshman G Nair
Mechanical Engineer | Python Developer
