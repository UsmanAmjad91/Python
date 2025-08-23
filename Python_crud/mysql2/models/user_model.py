from config.db import mysql

class UserModel:

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        cur.close()
        return data

    @staticmethod
    def get_by_id(user_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        data = cur.fetchone()
        cur.close()
        return data

    @staticmethod
    def insert(name, email, phone):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def update(user_id, name, email, phone):
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE users
            SET name=%s, email=%s, phone=%s
            WHERE id=%s
        """, (name, email, phone, user_id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete(user_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
        mysql.connection.commit()
        cur.close()
