from ketnoidb.ketnoi_mysql import connect_mysql

def update_danhmuc(madm, tendm_moi, mota_moi):
    """Cập nhật tên và mô tả danh mục theo mã danh mục"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối MySQL.")
        return

    try:
        cursor = conn.cursor()
        sql = "UPDATE danhmuc SET tendm = %s, mota = %s WHERE madm = %s"
        values = (tendm_moi, mota_moi, madm)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có mã {madm}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {madm}")

    except Exception as e:
        print(f"❌ Lỗi khi cập nhật danh mục: {e}")
    finally:
        cursor.close()
        conn.close()
