import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Informasi Perpustakaan")
        self.geometry("900x500")

        # Konfigurasi grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # =========================
        # FRAME KIRI - FORM INPUT
        # =========================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.label_judul = ctk.CTkLabel(
            self.frame_kiri,
            text="FORM DATA BUKU",
            font=("Arial", 20, "bold")
        )
        self.label_judul.pack(pady=20)

        # Judul Buku
        self.label_buku = ctk.CTkLabel(
            self.frame_kiri,
            text="Judul Buku"
        )
        self.label_buku.pack(
            anchor="w",
            padx=20
        )

        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan judul buku"
        )
        self.entry_judul.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # Penulis
        self.label_penulis = ctk.CTkLabel(
            self.frame_kiri,
            text="Penulis"
        )
        self.label_penulis.pack(
            anchor="w",
            padx=20
        )

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan nama penulis"
        )
        self.entry_penulis.pack(
            fill="x",
            padx=20,
            pady=(5, 15)
        )

        # Tahun Terbit
        self.label_tahun = ctk.CTkLabel(
            self.frame_kiri,
            text="Tahun Terbit"
        )
        self.label_tahun.pack(
            anchor="w",
            padx=20
        )

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan tahun terbit"
        )
        self.entry_tahun.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        # =========================
        # TOMBOL
        # =========================

        # Tombol Simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data"
        )
        self.btn_simpan.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Tombol Update
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="blue",
            hover_color="#0000CC"
        )
        self.btn_update.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Tombol Delete
        self.btn_delete = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="red",
            hover_color="#CC0000"
        )
        self.btn_delete.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # =========================
        # FRAME KANAN - TABEL DATA
        # =========================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0,
            column=1,
            padx=(0, 20),
            pady=20,
            sticky="nsew"
        )

        self.frame_kanan.grid_rowconfigure(1, weight=1)
        self.frame_kanan.grid_columnconfigure(0, weight=1)

        self.label_tabel = ctk.CTkLabel(
            self.frame_kanan,
            text="DAFTAR BUKU",
            font=("Arial", 20, "bold")
        )
        self.label_tabel.grid(
            row=0,
            column=0,
            pady=20
        )

        # Style tabel
        style = ttk.Style()
        style.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 11)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 11, "bold")
        )

        # Treeview
        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=(
                "id",
                "judul",
                "penulis",
                "tahun"
            ),
            show="headings"
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun Terbit")

        self.tabel.column("id", width=50)
        self.tabel.column("judul", width=180)
        self.tabel.column("penulis", width=150)
        self.tabel.column("tahun", width=100)

        self.tabel.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 20),
            sticky="nsew"
        )


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()