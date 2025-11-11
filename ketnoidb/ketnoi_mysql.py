import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Hàm kết nối tới MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Tên host, thường là localhost
            user='root',           # Tên người dùng MySQL
            password='thuy2005.',           # Mật khẩu MySQL (nếu có thì điền vào)
            database='qlthuocankhang'    # Tên database bạn muốn dùng
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print(f"❌ Lỗi kết nối MySQL: {e}")
        return None
