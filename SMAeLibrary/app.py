# Library nya
import pandas as pd
import numpy as np
import time
import datetime 
import openpyxl

# Settingan DataFramenya
file_path = "data\\database.xlsx"

df_masuk  = pd.read_excel(file_path, sheet_name="bukumasuk")
df_keluar = pd.read_excel(file_path, sheet_name="bukukeluar")

# Variabel tanggal dan waktu sekarang
today = datetime.date.today().strftime("%d/%m/%Y")
now = datetime.datetime.now().strftime("%H.%M")

# Settingan Pandas, biar menampilkan semua data di excel
pd.set_option('display.max_rows', None) # max_rows itu jumlah maksimum baris yang ditampilkan

# Tampilan Awal Aplikasi
print("----- SMAeLibrary -----")
print()
print("===============================")
print()
time.sleep(1.5)

# Loadingnya
print("Memuat aplikasi", end="", flush=True)
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1.5)

# Menu Utama Aplikasi
while True: # Kondisi loop biar bisa dipake terus
    print("\r", end="Menu:                       ") # \r fungsinya untuk timpa teks (secara simpelnya begitu)
    print() # Baris baru
    print("1. Lihat Database")
    print("2. Input Buku Masuk")
    print("3. Input Buku Keluar")
    print("4. Cek ID Buku")
    print("5. Keluar Aplikasi")
    print()

    pilihan = input("Pilih menu (1-5): ") # Apa yh...adalah pokoknya
    print()

    # Lihat Database
    if pilihan == "1":
        print()
        print("===============================") # Pembatasnya (begitulah kira-kira)
        print("Mau lihat yang mana?")
        print()
        print("1. Buku Masuk")
        print("2. Buku Keluar")
        print("3. Kembali")
        print()
        sub_pilihan = input("Pilih menu (1-3): ")
        print()

        if sub_pilihan == "1":
            print("===============================")
            print()
            print("Menampilkan database buku", end="", flush=True)
            for i in range(4):
                print(".", end="", flush=True)
                time.sleep(1.5)
            print()
            print(df_masuk.to_string(index=False)) 
            print()

        # to_string fungsinya mengonversi data di Excel menjadi string bawaan Python
        # 'index=False' itu fungsinya mencegah index bawaan Python/Pandas muncul

        elif sub_pilihan == "2":
            print("===============================")
            print()
            print("Menampilkan database buku", end="", flush=True)
            for i in range(4):
                print(".", end="", flush=True)
                time.sleep(1.5)
            print()
            print(df_keluar.to_string(index=False))
            print()
            
        elif sub_pilihan == "3":
            print("===============================")
            print()
            print("Kembali ke menu utama", end="", flush=True)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            continue

        else: # Kondisi alternatifnya.
            print("===============================")
            print()
            print("Data tidak ada / Pilihan tidak valid!")
            time.sleep(1)

    # Input Buku Masuk
    elif pilihan == "2":
        print("===============================")
        print()
        print("Memuat", end="", flush=True) # Loadingnya
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print()
        id_buku = input("Masukkan ID Buku: ") # Input id buku
        judul_buku = input("Masukkan Judul Buku: ") # Input judul buku
        penerbit = input("Masukkan Penerbit: ") # Input penerbit buku
        jumlah = input("Masukkan Jumlah Buku: ") # Input jumlah buku
        print("Gunakan Kode 'today' untuk tanggal hari ini") # Panduan kodenya kalau sampai hari ini
        tanggal_masuk = input("Masukkan Tanggal Masuk (HH/BB/TTTT): ") # Input tanggal masuk
        print("Gunakan Kode 'now' untuk jam sekarang") # Panduan kodenya kalau sampai jam sekarang
        jam = input("Masukkan Jam Masuk (MM.DD): ") # Input jam masuk
        print() # Baris baru
        time.sleep(1) # Delaynya

        if tanggal_masuk.lower() == "today": # Kalau inputnya today
            tanggal_masuk = today

        if jam.lower() == "now": # Kalau inputnya now
            jam = now
        
        # Ndk ada kondisi else, tetap lanjut kalau ndk pake kode

        print()
        m = pd.Series([id_buku, judul_buku, penerbit, jumlah, tanggal_masuk, jam], index=df_masuk.columns) 
        print("Konfirmasi: ")
        print(m) 
        print()
        confirm_masuk = input("Apakah data sudah benar? (ya/tidak): ")

        if confirm_masuk.lower() == "ya": # 'lower' fungsinya untuk mengubah inputan jadi huruf kecil semua supaya bisa lanjut
            print("Sedang memproses data", end="", flush=True) # Loading lagi
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1.5)

            df_masuk = pd.concat([df_masuk, pd.DataFrame([m])], ignore_index=True) # pd.concat fungsinya untuk menggabungkan Data yang diinput di Python ke Excel

            df_masuk["id_buku"] = df_masuk["id_buku"].astype(str)
            df_masuk["jumlah"] = df_masuk["jumlah"].astype(str)
            df_masuk["jam"] = df_masuk["jam"].astype(str) # Biar kolom jam, id buku, dan jumlahnya jadi string (fix bug kolom jam 'rrr,rrr' -> 'rrr.rrr')
            with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                df_masuk.to_excel(writer, sheet_name="bukumasuk", index=False)

            # Di bagian atas, diperlukan memanggil sintaks 'with pd.ExcelWriter' dan menggunakan library openpyxl (tidak perlu menggunakan sintaks 'import ...') yang berfungsi untuk membaca file Excelnya
            # Setelah itu, kita arahkan ke file_path dengan engine openpyxl, serta mengatur ke mode append yang fungsinya menambah data ke sheet yang sudah ada (mencegah duplikasi)
            # Terdapat 'if_sheet_exists="replace"' yang berfungsi untuk menulis ulang data baru
            # 'df_masuk.to_excel' fungsinya untuk memasukkan data Excelnya.

            print("\r", end="Data berhasil disimpan!         ", flush=True) # Notifikasi kalau datanya disimpan
            print()
            print("===============================")
            print()
            time.sleep(2)

        else:
            print()
            print("Data tidak disimpan.")
            print()
            print("===============================")
            print()
            time.sleep(1.5)

    # Input Buku Keluar
    elif pilihan == "3":
        print("===============================")
        print()
        print("Memuat", end="", flush=True) # Loading lagi
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print()
        id_buku = input("Masukkan ID Buku: ") # Input id buku
        judul_buku = input("Masukkan Judul Buku: ") # Input judul buku
        penerbit = input("Masukkan Penerbit: ") # Input penerbit buku
        jumlah = input("Masukkan Jumlah Buku: ") # Input jumlah buku
        alasan = input("Masukkan Alasan: ") # Input alasan
        print("Gunakan Kode 'today' untuk tanggal hari ini") # Panduan kodenya kalau sampai hari ini
        tanggal_keluar = input("Masukkan Tanggal Keluar (Format: HH/BB/TTTT): ") # Input tanggal keluar
        print("Gunakan Kode 'now' untuk jam sekarang") # Panduan kodenya kalau sampai jam sekarang
        jam = input("Masukkan Jam Keluar (Format: MM.DD): ") # Input jam keluar
        print()
        time.sleep(1) # Delaynya

        if tanggal_keluar.lower() == "today":
            tanggal_keluar = today

        if jam.lower() == "now":
            jam = now
        
        print()
        m = pd.Series([id_buku, judul_buku, penerbit, jumlah, alasan, tanggal_keluar, jam], index=df_keluar.columns)
        print("Konfirmasi: ")
        print(m) 
        print()
        confirm_keluar = input("Apakah data sudah benar? (ya/tidak): ")

        if confirm_keluar.lower() == "ya":
            print("Sedang memproses data", end="", flush=True)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1.5)

            df_keluar = pd.concat([df_keluar, pd.DataFrame([m])], ignore_index=True)

            df_keluar["jumlah"] = df_keluar["jumlah"].astype(str)
            df_keluar["jam"] = df_keluar["jam"].astype(str)
            with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                df_keluar.to_excel(writer, sheet_name="bukukeluar", index=False)

            print("\r", end="Data berhasil disimpan!         ", flush=True)
            print()
            print("===============================")
            print()
            time.sleep(2)

        else:
            print()
            print("Data tidak disimpan.")
            print()
            print("===============================")
            print()
            time.sleep(1)

    # Cek ID Buku
    elif pilihan == "4":
        print("===============================")
        print()
        print("Mau lihat yang mana?")
        print("1. Buku Masuk")
        print("2. Buku Keluar")
        print("3. Kembali")
        print()
        cekid = input("Pilih menu (1-3): ")
        print()

        if cekid == "1":
            print("===============================")
            print()
            print("Mengambil ID Buku pada Database", end="", flush=True)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            print()
            idbuku = df_masuk["id_buku"].tolist() # tolist fungsinya mengonversi data di Excel menjadi list bawaan Python
            print("\nID Buku: ") # \n fungsinya baris baru (sama kyk 'print()')
            print(idbuku)
            print()
            print("===============================")
            print()
            time.sleep(1)

        elif cekid == "2":
            print("===============================")
            print()
            print("Mengambil ID Buku pada Database", end="", flush=True)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            idbuku = df_keluar["id_buku"].tolist()
            print()
            print("\nID Buku: ") # \n fungsinya baris baru (sama kyk 'print()')
            print(idbuku)
            print()
            print("===============================")
            print()
            time.sleep(1)

        elif cekid == "3":
            print("===============================")
            print()
            print("Kembali ke Menu Utama", end="", flush=True)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            continue

        else:
            print("===============================")
            print()
            print("Data tidak ada / Pilihan tidak valid!")
            time.sleep(1)

    # Keluar Aplikasi
    elif pilihan == "5":
        print("===============================")
        print()
        print("Keluar dari aplikasi", end="", flush=True)
        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(1)
        break # Untuk menghentikan loop while True dan menghentikan programnya

    # Kondisi alternatif
    else:
        print()
        print("Pilihan tidak valid!")
        print()
        time.sleep(1)