from ketnoidb.ketnoi_mysql import connect_mysql

def delete_danhmuc(madm):
    """Xóa 1 danh mục theo mã danh mục (madm)"""
    conn = connect_mysql()
    if conn is None:
        print("Không thể kết nối MySQL.")
        return

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE madm = %s"
        cursor.execute(sql, (madm,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có mã {madm}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {madm}")

    except Exception as e:
        print(f"❌ Lỗi khi xóa danh mục: {e}")
    finally:
        cursor.close()
        conn.close()
