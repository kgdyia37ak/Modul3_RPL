
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

            # Mengubah password menjadi hash SHA-256
            password_hash = self.hash_password(password)

            # Mencari username dan password yang cocok
            query = """
                SELECT id_user, username, role
                FROM users
                WHERE username = %s AND password = %s
            """

            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()

            return user

        return None

    # TUGAS MODUL 7: REGISTER USER
    def register_user(self, username, password, role):
        if self.conn:
            cursor = self.conn.cursor()

            # Memeriksa apakah semua data sudah diisi
            if not username or not password:
                cursor.close()
                return False

            # Memastikan role yang dimasukkan valid
            if role not in ("admin", "anggota"):
                cursor.close()
                return False

            # Mengubah password menjadi hash SHA-256
            password_hash = self.hash_password(password)

            # Menyimpan akun baru ke database
            query = """
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """

            try:
                cursor.execute(query, (username, password_hash, role))
                self.conn.commit()
                cursor.close()
                return True

            except Exception:
                self.conn.rollback()
                cursor.close()
                return False

        return False