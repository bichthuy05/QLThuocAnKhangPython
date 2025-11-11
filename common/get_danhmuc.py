from ketnoidb.ketnoi_mysql import connect_mysql

def get_all_danhmuc():
    """Lấy danh sách tất cả danh mục"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối MySQL.")
        return []

    try:
        cursor = conn.cursor(dictionary=True)  # trả về kết quả dạng dict
        sql = "SELECT madm, tendm, mota, trangthai FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()

        print("✅ Danh sách danh mục:")
        for dm in result:
            print(f"ID: {dm['madm']} | Tên: {dm['tendm']} | Mô tả: {dm['mota']} | Trạng thái: {dm['trangthai']}")

        return result

    except Exception as e:
        print(f"❌ Lỗi khi lấy danh sách danh mục: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
