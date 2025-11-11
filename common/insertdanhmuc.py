from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(tendm, mota):
    """Thêm mới 1 danh mục vào bảng danhmuc"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối đến MySQL.")
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)"
        values = (tendm, mota)
        cursor.execute(sql, values)
        conn.commit()  # lưu thay đổi
        print(f"✅ Đã thêm danh mục: {tendm}")
    except Exception as e:
        print(f"❌ Lỗi khi thêm danh mục: {e}")
    finally:
        cursor.close()
        conn.close()
