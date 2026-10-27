import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Data Anggota Perpustakaan")
        self.geometry("900x500")

        # Konfigurasi grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # =========================
        # FRAME KIRI - FORM ANGGOTA
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
            text="FORM DATA ANGGOTA",
            font=("Arial", 20, "bold")
        )
        self.label_judul.pack(pady=20)

        # Nama Anggota
        self.label_nama = ctk.CTkLabel(
            self.frame_kiri,
            text="Nama Anggota"
        )
        self.label_nama.pack(
            anchor="w",
            padx=20
        )

        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan nama anggota"
        )
        self.entry_nama.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

        # Alamat
        self.label_alamat = ctk.CTkLabel(
            self.frame_kiri,
            text="Alamat"
        )
        self.label_alamat.pack(
            anchor="w",
            padx=20
        )

        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan alamat anggota"
        )
        self.entry_alamat.pack(
            fill="x",
            padx=20,
            pady=(5, 20)
        )

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
        # FRAME KANAN - TABEL ANGGOTA
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
            text="DAFTAR ANGGOTA",
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

        # Treeview anggota
        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=(
                "id_anggota",
                "nama",
                "alamat"
            ),
            show="headings"
        )

        self.tabel.heading(
            "id_anggota",
            text="ID Anggota"
        )

        self.tabel.heading(
            "nama",
            text="Nama Anggota"
        )

        self.tabel.heading(
            "alamat",
            text="Alamat"
        )

        self.tabel.column(
            "id_anggota",
            width=100
        )

        self.tabel.column(
            "nama",
            width=180
        )

        self.tabel.column(
            "alamat",
            width=250
        )

        self.tabel.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 20),
            sticky="nsew"
        )


if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()