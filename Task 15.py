import pandas as pd

print("\n\nSESSION 15 - COUNTRIES DATASET")

print("\n\nQ. Load the Countries Dataset")

# Reading the CSV file
df = pd.read_csv("Countries.csv")

# Displaying the dataset
print(df)

#=====================================================================

print("\n\nQ. Display First 5 Rows")

# Displaying first five rows
print(df.head())

#=====================================================================

print("\n\nQ. Display Last 5 Rows")

# Displaying last five rows
print(df.tail())

#=====================================================================

print("\n\nQ. Shape of Dataset")

# Displaying rows and columns
print("Shape :", df.shape)

#=====================================================================

print("\n\nQ. Column Names")

# Displaying all column names
print(df.columns)

#=====================================================================

print("\n\nQ. Dataset Information")

# Displaying complete information
df.info()

#=====================================================================

print("\n\nQ. Statistical Summary")

# Displaying statistics of numerical columns
print(df.describe())

#=====================================================================

print("\n\nQ. Data Types")

# Displaying datatype of each column
print(df.dtypes)

#=====================================================================

print("\n\nQ. Missing Values")

# Counting missing values
print(df.isnull().sum())

#=====================================================================

# Displaying number of unique values
print("\nUnique Values:")
print(df.nunique())

# Displaying five random rows
print("\n5 Random Records:")
print(df.sample(5))

# Taking column name from user
column = input("\nEnter column name to count unique values: ")

# Checking if column exists
if column in df.columns:

    print(df[column].value_counts())

else:

    print("Column not found!")

#=====================================================================