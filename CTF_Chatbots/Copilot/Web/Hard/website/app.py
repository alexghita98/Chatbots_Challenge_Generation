from flask import Flask, request, render_template_string
import sqlite3
import time

app = Flask(__name__)

FLAG = "flag{blind_sql_injection_master}"

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS secrets (flag TEXT)')
    c.execute('DELETE FROM products')
    c.execute('DELETE FROM secrets')
    c.executemany('INSERT INTO products (name) VALUES (?)', [
        ('Widget A',), ('Widget B',), ('Widget C',)
    ])
    c.execute('INSERT INTO secrets (flag) VALUES (?)', (FLAG,))
    conn.commit()
    conn.close()

init_db()

search_page = '''
<!doctype html>
<title>Product Search</title>
<h2>Search Products</h2>
<form method="GET">
  <input type="text" name="q" placeholder="Search term">
  <input type="submit" value="Search">
</form>
<p>{{ result }}</p>
'''

@app.route('/search')
def search():
    query = request.args.get('q', '')
    result = "No products found."
    try:
        conn = sqlite3.connect('products.db')
        c = conn.cursor()

        # Check for time-based injection pattern
        if "sleep(" in query.lower():
            try:
                # Extract sleep duration from payload
                duration = int(query.lower().split("sleep(")[1].split(")")[0])
                time.sleep(duration)
            except:
                pass

        sql = f"SELECT name FROM products WHERE name LIKE '%{query}%'"
        c.execute(sql)
        rows = c.fetchall()
        if rows:
            result = "<br>".join([row[0] for row in rows])
        conn.close()
    except Exception:
        pass  # Suppress errors
    return render_template_string(search_page, result=result)

# No app.run() — Gunicorn will handle it
