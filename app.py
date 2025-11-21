from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Required for sessions (logging in)

# --- HELPER FUNCTION: CONNECT TO DATABASE ---
def get_db():
    conn = sqlite3.connect('travel.db')
    conn.row_factory = sqlite3.Row # Allows accessing columns by name (row['email'])
    return conn

# --- ROUTE 1: HOME PAGE ---
@app.route('/')
def home():
    # Check if user is logged in
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return render_template('home.html')

# --- ROUTE 2: LOGIN / REGISTER ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db()
        # Check if user exists
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        
        if user:
            # User exists, check password (in a real app, hash this!)
            if user['password'] == password:
                session['user'] = email # Login successful
                return redirect('/')
            else:
                flash('Wrong password!')
        else:
            # User does not exist, create new account automatically
            conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
            conn.commit()
            session['user'] = email # Login the new user
            flash('Account created! You are now logged in.')
            
        conn.close()
        return redirect('/')
        
    return render_template('login.html')

# --- ROUTE 3: LOGOUT ---
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.')
    return redirect('/login')

# --- ROUTE 4: SEARCH (FLIGHTS & HOTELS) ---
@app.route('/search', methods=['POST'])
def search():
    search_type = request.form['type']
    conn = get_db()
    results = []

    if search_type == 'flight':
        # .strip() removes spaces, .title() makes "delhi" -> "Delhi"
        source = request.form['source'].strip().title() 
        dest = request.form['destination'].strip().title()
        
        # Search strictly by Source AND Destination
        results = conn.execute('SELECT * FROM flights WHERE source = ? AND destination = ?', (source, dest)).fetchall()
        if not results:
            flash(f'No flights found from {source} to {dest}. Try checking your spelling.')

    elif search_type == 'hotel':
        location = request.form['location'].strip().title()
        # Search by location
        results = conn.execute('SELECT * FROM hotels WHERE location = ?', (location,)).fetchall()
        if not results:
            flash(f'No hotels found in {location}. We currently only have Mumbai, Delhi, and Goa.')

    conn.close()
    return render_template('home.html', results=results, user=session.get('user'))

# --- ROUTE 5: BOOKING ---
@app.route('/book', methods=['POST'])
def book():
    if 'user' not in session:
        flash('Please login to book!')
        return redirect('/login')

    item_id = request.form['id']
    item_type = request.form['type']
    user_email = session['user']
    
    conn = get_db()
    
    # Get details to save in booking history
    details = ""
    if item_type == 'flight':
        item = conn.execute('SELECT * FROM flights WHERE id = ?', (item_id,)).fetchone()
        details = f"{item['airline']} : {item['source']} -> {item['destination']}"
    else:
        item = conn.execute('SELECT * FROM hotels WHERE id = ?', (item_id,)).fetchone()
        details = f"{item['name']} in {item['location']}"

    # Save to database
    conn.execute('INSERT INTO bookings (user_email, type, details) VALUES (?, ?, ?)', 
                 (user_email, item_type, details))
    conn.commit()
    conn.close()
    
    flash('Booking Successful! View it in "My Bookings".')
    return redirect('/bookings')

# --- ROUTE 6: MY BOOKINGS PAGE ---
@app.route('/bookings')
def my_bookings():
    if 'user' not in session:
        return redirect('/login')
        
    conn = get_db()
    user_bookings = conn.execute('SELECT * FROM bookings WHERE user_email = ?', (session['user'],)).fetchall()
    conn.close()
    
    return render_template('bookings.html', bookings=user_bookings)

if __name__ == '__main__':
    app.run(debug=True)