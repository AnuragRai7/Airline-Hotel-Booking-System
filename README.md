# ✈️ Airline & Hotel Booking System

A full-stack web application built with **Python (Flask)** and **SQLite** that allows users to search for flights, browse hotels, and manage travel bookings in real-time.

## 🚀 Features
* **User Authentication:** Secure Login/Registration system with session management.
* **Dynamic Search:** Search functionality for Flights (Source ➝ Destination) and Hotels (Location).
* **Booking Engine:** Users can book tickets/rooms which are saved to their personal dashboard.
* **Case-Insensitive Search:** Smart search algorithms handle capitalization errors (e.g., "delhi" matches "Delhi").
* **Responsive UI:** Built with Bootstrap 5 for mobile and desktop compatibility.

## 🛠️ Tech Stack
* **Backend:** Python 3, Flask
* **Database:** SQLite (Relational Database)
* **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templating

## ⚙️ Installation & Setup
If you want to run this project locally, follow these steps:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Airline-Hotel-Booking-System.git](https://github.com/YOUR_USERNAME/Airline-Hotel-Booking-System.git)
    cd Airline-Hotel-Booking-System
    ```

2.  **Install Dependencies**
    ```bash
    pip install flask
    ```

3.  **Initialize Database**
    Run the setup script to create tables and load dummy data:
    ```bash
    python setup_database.py
    ```

4.  **Run the Application**
    ```bash
    python app.py
    ```

5.  **Access the App**
    Open your browser and go to: `http://127.0.0.1:5000`

## 📸 Screenshots

## 📝 Learning Outcomes
This project demonstrates understanding of:
* **CRUD Operations** (Create, Read, Update, Delete)
* **MVC Architecture** (Model-View-Controller)
* **Relational Database Design**
* **RESTful Routing**
