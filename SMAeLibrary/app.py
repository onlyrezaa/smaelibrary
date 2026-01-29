# Library nya
import pandas as pd
import numpy as np
import time
import os

# Settingan DataFramenya
dt = pd.read_excel("data\\database.xlsx")
pd.set_option('display.max_rows', None)

print("----- SMAeLibrary -----")
print()
print("===============================")
print()
time.sleep(1.5)

print("Memuat aplikasi", end="", flush=True)
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1.5)

while True:
    print("\rMenu:                     ")
    print()
    print("1. Lihat Database")
    print("2. Input Buku Masuk")
    print("3. Input Buku Keluar")
    print("4. Keluar Aplikasi")
    print()

    pilihan = int(input("Pilih menu (1-4): "))
    print()

    if pilihan == 1:
        print()
        print("Menampilkan database buku", end="", flush=True)
        for i in range(4):
            print(".", end="", flush=True)
            time.sleep(3)
        print()
        print(dt.to_string(index=False))
        print()
        
    elif pilihan == 2:
        print()
        print("Memuat", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1.5)
        user = input("\nMasukkan nama Peminjam: ")
        buku = input("Masukkan judul buku: ")
        tanggal = input("Masukkan tanggal pinjam: ")
        jam = input("Masukkan jam pinjam: ")
        print()
        time.sleep(5)

        s = pd.Series([user, buku, tanggal, jam], index=dt.columns, sheet_name="bukukeluar")
        print("Konfirmasi: ")
        print(s) 
        print()
        confirm = input("Apakah data sudah benar? (ya/tidak): ")

    elif pilihan == 3:
        print()
        print("Fitur input buku keluar belum tersedia.")
        time.sleep(1)

    elif pilihan == 4:
        print("Keluar dari aplikasi", end="", flush=True)
        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(1.5)
        break

    else:
        print()
        print("Pilihan tidak valid!")
        time.sleep(1)

    if confirm == "ya":
        print("Sedang memproses data", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1.5)
            dt = pd.concat([dt, pd.DataFrame([s])], ignore_index=True)
            dt.to_excel("data\\database.xlsx", index=False, sheet_name='bukukeluar')
            print("\nData berhasil disimpan!             ")
    else:
        print()
        print("Data tidak disimpan.")
        time.sleep(1.5)