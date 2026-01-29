import pandas as pd
import numpy as np
import time
import os

dt = pd.read_excel("data\\database.xlsx")

print("----- SMAeLibrary -----")
print()
print("===============================")
print()
time.sleep(1.5)

print("Memuat aplikasi", end="", flush=True)
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1.5)

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
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1.5)
    print()
    print(dt.head())

elif pilihan == 2:
    print()
    print("Fitur input buku masuk belum tersedia.")
    time.sleep(1.5)

elif pilihan == 3:
    print()
    print("Fitur input buku keluar belum tersedia.")
    time.sleep(1)

elif pilihan == 4:
    print("Keluar dari aplikasi...")

else:
    print()
    print("Pilihan tidak valid!")
    time.sleep(1)
