
# Rendra 024
import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Mengubah password biasa menjadi hash SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)

            # Mengubah password yang dimasukkan menjadi hash
            password_hash = self.hash_password(password)

            # Mencari username dan password yang cocok di database
            query = """
                SELECT id_user, username, role
                FROM users
                WHERE username = %s AND password = %s
            """

            # Mengirimkan username dan password hash ke database
            cursor.execute(query, (username, password_hash))

            # Mengambil data pengguna jika login berhasil
            user = cursor.fetchone()

            cursor.close()

            return user

        return None