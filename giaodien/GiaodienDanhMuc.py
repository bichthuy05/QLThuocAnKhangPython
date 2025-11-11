import tkinter as tk
from tkinter import ttk, messagebox
from ketnoidb.ketnoi_mysql import connect_mysql


class DanhMucApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Danh mục")
        self.root.geometry("700x400")

        # --- Nhãn và ô nhập ---
        tk.Label(root, text="Tên danh mục:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(root, text="Mô tả:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.tendm_entry = tk.Entry(root, width=40)
        self.mota_entry = tk.Entry(root, width=40)

        self.tendm_entry.grid(row=0, column=1, padx=10, pady=5)
        self.mota_entry.grid(row=1, column=1, padx=10, pady=5)

        # --- Nút chức năng ---
        tk.Button(root, text="Thêm", bg="#4CAF50", fg="white").grid(row=0, column=2, padx=10)
        tk.Button(root, text="Sửa", bg="#2196F3", fg="white").grid(row=1, column=2, padx=10)
        tk.Button(root, text="Xóa", bg="#f44336", fg="white").grid(row=2, column=2, padx=10)
        tk.Button(root, text="Tải lại", bg="#9C27B0", fg="white", command=self.load_danhmuc).grid(row=3, column=2, padx=10)

        # --- Bảng hiển thị danh mục ---
        self.tree = ttk.Treeview(root, columns=("madm", "tendm", "mota"), show="headings")
        self.tree.heading("madm", text="Mã")
        self.tree.heading("tendm", text="Tên danh mục")
        self.tree.heading("mota", text="Mô tả")
        self.tree.column("madm", width=50, anchor="center")

        # Gắn sự kiện chọn dòng
        self.tree.bind("<<TreeviewSelect>>", self.select_row)
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Gọi hàm load dữ liệu khi khởi động
        self.load_danhmuc()

    def select_row(self, event):
        """Khi chọn dòng trên TreeView"""
        selected = self.tree.selection()
        if selected:
            madm, tendm, mota = self.tree.item(selected[0])["values"]
            self.tendm_entry.delete(0, tk.END)
            self.tendm_entry.insert(0, tendm)
            self.mota_entry.delete(0, tk.END)
            self.mota_entry.insert(0, mota)

    def load_danhmuc(self):
        """Hiển thị toàn bộ danh mục"""
        conn = connect_mysql()
        if not conn:
            messagebox.showerror("Lỗi", "Không thể kết nối MySQL!")
            return

        cursor = conn.cursor()
        cursor.execute("SELECT madm, tendm, mota FROM danhmuc")
        rows = cursor.fetchall()

        # Xóa dữ liệu cũ trong TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Thêm dữ liệu mới
        for row in rows:
            self.tree.insert("", tk.END, values=row)

        cursor.close()
        conn.close()


# --- Chạy giao diện ---
if __name__ == "__main__":
    root = tk.Tk()
    app = DanhMucApp(root)
    root.mainloop()
