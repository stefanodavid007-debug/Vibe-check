import sqlite3
import time

class Database:
    def __init__(self, db_name=":memory:"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._setup()
        self.query_count = 0

    def _setup(self):
        self.cursor.execute("CREATE TABLE categories (id INTEGER PRIMARY KEY, name TEXT)")
        self.cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category_id INTEGER)")

        categories = [(1, "Electronics"), (2, "Clothing"), (3, "Books")]
        self.cursor.executemany("INSERT INTO categories VALUES (?, ?)", categories)

        products = [(i, f"Product {i}", (i % 3) + 1) for i in range(1, 101)]
        self.cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", products)
        self.conn.commit()

    def get_products(self):
        self.query_count += 1
        self.cursor.execute("SELECT id, name, category_id FROM products")
        return self.cursor.fetchall()

    def get_category_name(self, category_id):
        self.query_count += 1
        # Simulate network latency
        time.sleep(0.005)
        self.cursor.execute("SELECT name FROM categories WHERE id = ?", (category_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_categories_batch(self, category_ids):
        self.query_count += 1
        # Simulate network latency
        time.sleep(0.005)
        placeholders = ','.join(['?'] * len(category_ids))
        self.cursor.execute(f"SELECT id, name FROM categories WHERE id IN ({placeholders})", list(category_ids))
        return dict(self.cursor.fetchall())
