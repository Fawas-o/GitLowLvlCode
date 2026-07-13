#all me, trynig to learn through exp
import pandas as pd

print("----Loading----")
try:
    df = pd.read_csv('lung_cancer.csv')
    print(f"These are the total numbers of rows and columns {df.shape}")

    print(f"\n----These are the structures of the database----")
    print()
    print(f"\n----Dataset values----")
    df.info()
    print()
    print("Short preview of 5 Rows")
    print(df.head(5))

except FileNotFoundError:
    print("File could not be loaded") 
    