# 1. Import Pandas
import pandas as pd


# 2. Creating a DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 21, 19],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print("\n1. CREATING A DATAFRAME")
print(df)


# 3. Reading a Dataset

df.to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")

print("\n2. READING A DATASET")
print(df)


# 4. Viewing Data

print("\n3. FIRST 5 ROWS")
print(df.head())

print("\n4. FIRST 3 ROWS")
print(df.head(3))

print("\n5. LAST 5 ROWS")
print(df.tail())

print("\n6. LAST 2 ROWS")
print(df.tail(2))


# 5. Data Types

print("\n7. DATA TYPES")
print(df.dtypes)


# 6. DataFrame Information

print("\n8. DATAFRAME INFORMATION")
df.info()


# 7. Statistical Summary

print("\n9. STATISTICAL SUMMARY")
print(df.describe())


# 8. Selecting Columns

print("\n10. SELECTING NAME COLUMN")
print(df["Name"])

print("\n11. SELECTING AGE COLUMN")
print(df["Age"])

print("\n12. SELECTING MARKS COLUMN")
print(df["Marks"])


# Selecting Multiple Columns

print("\n13. SELECTING MULTIPLE COLUMNS")
print(df[["Name", "Marks"]])

# Using loc to select the first row
print("\n14. SELECTING FIRST ROW USING loc")
print(df.loc[0])


# Using iloc to select the first row
print("\n15. SELECTING FIRST ROW USING iloc")
print(df.iloc[0])


# Selecting the first row and second column
print("\n16. FIRST ROW AND SECOND COLUMN")
print(df.iloc[0, 1])


# Selecting the first two rows using loc
print("\n17. FIRST TWO ROWS USING loc")
print(df.loc[0:1])


# Selecting the first two rows using iloc
print("\n18. FIRST TWO ROWS USING iloc")
print(df.iloc[0:2])


# Selecting a specific column from a row
print("\n19. SELECTING NAME USING loc")
print(df.loc[0, "Name"])


# Selecting Name and Marks columns
print("\n20. SELECTING MULTIPLE COLUMNS")
print(df[["Name", "Marks"]])

print("\nALL TASKS COMPLETED!")

# Creating a DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Marks": [45, 90, 75, 40]
}


print("Original DataFrame:")
print(df)

# Students with marks greater than or equal to 50
passed = df[df["Marks"] >= 50]

print("\nStudents Who Passed:")
print(passed)

# Students with marks less than 50
failed = df[df["Marks"] < 50]

print("\nStudents Who Failed:")
print(failed)


# Adding City column
df["City"] = ["Karachi", "Lahore", "Karachi"]
print("\nDataFrame After Adding City Column:")
print(df)


# Creating a new column using calculations
df["Bonus Marks"] = df["Marks"] + 5

print("\nDataFrame After Adding Bonus Marks:")
print(df)

# Creating a DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Age": [20, 22, 21, 23],
    "Marks": [45, 80, 65, 90]
}

df = pd.DataFrame(data)

# 11. Adding a New Column

df["City"] = ["Karachi", "Lahore", "Karachi", "Islamabad"]

print("11. Adding a New Column:")
print(df)


# Adding a column using calculations

df["Bonus Marks"] = df["Marks"] + 5

print("\nAdding Bonus Marks:")
print(df)


# 12. Updating Values

# Changing Ali's marks from 45 to 55

df.loc[0, "Marks"] = 55

print("\n12. Updating Values:")
print(df)


# 13. Deleting Rows and Columns

# Delete the Age column

df = df.drop("Age", axis=1)

print("\n13. Deleting a Column:")
print(df)

# Creating a DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Ali"],
    "Age": [20, 22, 21, None, 20],
    "Marks": [45, 80, 65, 90, 45],
    "City": ["Karachi", "Lahore", "Karachi", "Islamabad", "Karachi"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 13. Deleting Rows and Columns

# Delete a Column
df = df.drop("City", axis=1)

print("\n13. Deleting a Column:")
print(df)

# Delete a Row
df = df.drop(2, axis=0)

print("\nDeleting a Row:")
print(df)


# 14. Handling Missing Values

# Check Missing Values
print("\n14. Check Missing Values:")
print(df.isnull())

print("\nTotal Missing Values:")
print(df.isnull().sum())

# Remove Missing Values
df_removed = df.dropna()

print("\nRemove Missing Values:")
print(df_removed)

# Fill Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nFill Missing Values:")
print(df)


# 15. Handling Duplicate Data

# Check Duplicate Rows
print("\n15. Duplicate Rows:")
print(df.duplicated())

# Remove Duplicate Rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)


# 16. Sorting Data

# Sort by Marks in Ascending Order
print("\n16. Sorting by Marks (Ascending):")
print(df.sort_values(by="Marks"))

# Sort by Marks in Descending Order
print("\nSorting by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))


# 17. Aggregation and GroupBy

# Sum
print("\n17. Sum of Marks:")
print(df["Marks"].sum())

# Average
print("\nAverage Marks:")
print(df["Marks"].mean())

# Maximum
print("\nMaximum Marks:")
print(df["Marks"].max())

# Count
print("\nCount of Marks:")
print(df["Marks"].count())

# Minimum
print("\nMinimum Marks:")
print(df["Marks"].min())


# GroupBy
print("\nGroupBy City:")

df["City"] = ["Karachi", "Lahore", "Karachi", "Islamabad"][:len(df)]

print(df.groupby("City")["Marks"].sum())

# 18. COMBINING DATAFRAMES
# Creating First DataFrame
df1 = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Marks": [80, 90, 75]
})

# Creating Second DataFrame
df2 = pd.DataFrame({
    "Name": ["Ayesha", "Hamza", "Zara"],
    "Marks": [85, 70, 95]
})


# 1. CONCAT()

print("\n18. COMBINING DATAFRAMES USING CONCAT()")

df_concat = pd.concat([df1, df2], ignore_index=True)

print(df_concat)


# 2. MERGE()

print("\nCOMBINING DATAFRAMES USING MERGE()")

df3 = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 21, 19]
})

df4 = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "City": ["Karachi", "Lahore", "Islamabad"]
})

df_merge = pd.merge(df3, df4, on="Name")

print(df_merge)