import pandas as pd

print("Pandas imported successfully!")
# q2
data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 21, 19],
    "Marks": [80, 90, 75]
}
df = pd.DataFrame(data)

print(df)

# q3
print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nShape:")
print(df.shape)