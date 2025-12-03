"""User service with SQL injection vulnerability.

This file intentionally contains a SQL injection vulnerability
for demonstration purposes in the GHAS Campaigns + Autofix video.

DO NOT use this code in production!
"""

import sqlite3


class Database:
    def __init__(self, db_path='users.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
    
    def execute(self, query, params=None):
        if params:
            return self.cursor.execute(query, params)
        return self.cursor.execute(query)
    
    def close(self):
        self.connection.close()


db = Database()


def get_user(username):
    """Vulnerable function - SQL injection via f-string interpolation."""
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return db.execute(query)


def get_user_by_id(user_id):
    """Another vulnerable function - SQL injection via string concatenation."""
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return db.execute(query)


def search_users(search_term):
    """Vulnerable search function."""
    query = f"SELECT * FROM users WHERE name LIKE '%{search_term}%'"
    return db.execute(query)


def get_orders_for_user(username):
    """Another SQL injection vulnerability."""
    query = "SELECT o.* FROM orders o JOIN users u ON o.user_id = u.id WHERE u.name = '" + username + "'"
    return db.execute(query)
