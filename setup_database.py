import sqlite3

# This connects to a file named 'travel.db'. 
# If it doesn't exist, it creates it automatically.
conn = sqlite3.connect('travel.db')
cursor = conn.cursor()

print("Creating Database Tables...")

# 1. Create USERS Table (To store login info)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# 2. Create FLIGHTS Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        airline TEXT NOT NULL,
        source TEXT NOT NULL,
        destination TEXT NOT NULL,
        price INTEGER NOT NULL,
        date TEXT NOT NULL
    )
''')

# 3. Create HOTELS Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        price INTEGER NOT NULL,
        rating TEXT
    )
''')

# 4. Create BOOKINGS Table (To track what users bought)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT NOT NULL,
        type TEXT NOT NULL,  -- 'flight' or 'hotel'
        details TEXT NOT NULL
    )
''')

print("Tables created successfully!")

# --- INSERTING MOCK DATA (So your app isn't empty) ---
print("Inserting Fake Data...")

# clear old data so we don't duplicate if we run this twice
cursor.execute("DELETE FROM flights") 
cursor.execute("DELETE FROM hotels")

# Add Dummy Flights
flights_data = [
    ('IndiGo', 'Delhi', 'Mumbai', 4500, '2025-12-01'),
    ('Air India', 'Delhi', 'Bangalore', 6200, '2025-12-01'),
    ('Vistara', 'Mumbai', 'Goa', 3000, '2025-12-02'),
    ('SpiceJet', 'Delhi', 'Mumbai', 4200, '2025-12-01')
]
cursor.executemany("INSERT INTO flights (airline, source, destination, price, date) VALUES (?, ?, ?, ?, ?)", flights_data)

# Add Dummy Hotels
hotels_data = [
    ('Taj Palace', 'Mumbai', 12000, '5 Star'),
    ('Holiday Inn', 'Delhi', 4000, '4 Star'),
    ('Sunshine Resort', 'Goa', 2500, '3 Star')
]
cursor.executemany("INSERT INTO hotels (name, location, price, rating) VALUES (?, ?, ?, ?)", hotels_data)

conn.commit()
conn.close()
print("Database setup complete! A file named 'travel.db' should now appear.")