import pandas as pd
import numpy as np
import time
import os



df = pd.read_excel("data\\database.xlsx")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(2)

print()
print()
print(df.head())