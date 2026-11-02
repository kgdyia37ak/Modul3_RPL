# Rendra Akbar Fauzi_F5212510024

import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        # Menyimpan role pengguna yang sedang login
        self.user_role = user_role

        # Membuat objek model untuk mengakses database buku
        self.model = BukuModel()

        # Membuat tampilan aplikasi perpustakaan
        self.view = BukuView()

        # Menampilkan role pengguna pada judul aplikasi
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # Menghubungkan tombol Simpan dengan fungsi simpan_data
        self.view.btn_simpan.configure(command=self.simpan_data)

        # Menghubungkan tombol Update dengan fungsi update_data
        self.view.btn_update.configure(command=self.update_data)

        # Menghubungkan tombol Hapus dengan fungsi hapus_data
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Menghubungkan tombol Logout dengan fungsi logout
        self.view.btn_logout.configure(command=self.logout)

        # Memeriksa hak akses pengguna
        # TUGAS MODUL 7: OTORISASI UPDATE DAN DELETE
        if self.user_role != "admin":
            # Anggota tidak boleh menambah, mengubah, atau menghapus buku
            self.view.btn_simpan.configure(state="disabled")
            self.view.btn_update.configure(state="disabled")
            self.view.btn_hapus.configure(state="disabled")

            # Anggota hanya dapat melihat daftar buku
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Menampilkan data buku dari database ke tabel
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Menghapus seluruh isi tabel sebelum memuat data terbaru
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil semua data buku dari database
        data_buku = self.model.get_all_buku()

        # Memasukkan setiap data buku ke dalam tabel
        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        # Memastikan hanya admin yang dapat menambah buku
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menambah data!"
            )
            return

        # Mengambil isi dari setiap kolom input
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Memeriksa apakah semua kolom sudah diisi
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Menyimpan data buku melalui model
        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            # Mengosongkan kolom input setelah berhasil menyimpan
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            # Memperbarui tampilan tabel
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data."
            )

    def update_data(self):
        # Memastikan hanya admin yang dapat mengubah buku
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk mengubah data!"
            )
            return

        # Mengambil baris yang dipilih pada tabel
        pilihan = self.view.tabel.selection()

        # Memeriksa apakah pengguna sudah memilih buku
        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diubah!"
            )
            return

        # Mengambil data dari baris yang dipilih
        data = self.view.tabel.item(pilihan[0], "values")

        # Mengambil ID buku dari kolom pertama
        id_buku = data[0]

        # Mengambil data baru dari kolom input
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Memeriksa apakah semua kolom sudah diisi
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Mengubah data buku melalui model
        if self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )

            # Mengosongkan kolom input
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            # Memuat ulang data pada tabel
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal memperbarui data buku."
            )

    def hapus_data(self):
        # Memastikan hanya admin yang dapat menghapus buku
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menghapus data!"
            )
            return

        # Mengambil baris yang dipilih pada tabel
        pilihan = self.view.tabel.selection()

        # Memeriksa apakah ada buku yang dipilih
        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!"
            )
            return

        # Mengambil data dari baris yang dipilih
        data = self.view.tabel.item(pilihan[0], "values")

        # Mengambil ID buku
        id_buku = data[0]

        # Meminta konfirmasi sebelum menghapus data
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus buku ini?"
        )

        if konfirmasi:
            # Menghapus data buku melalui model
            if self.model.delete_buku(id_buku):
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil dihapus!"
                )

                # Memperbarui tampilan tabel
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error",
                    "Gagal menghapus data buku."
                )
    # TUGAS MODUL 7: LOGOUT
    def logout(self):
        # Menutup tampilan perpustakaan
        self.view.destroy()

        # Memanggil halaman login kembali
        from controllers.auth_controller import AuthController

        app_login = AuthController()
        app_login.run()

    def run(self):
        # Menjalankan aplikasi dan menampilkan jendela
        self.view.mainloop()


if __name__ == "__main__":
    app = BukuController()
    app.run()