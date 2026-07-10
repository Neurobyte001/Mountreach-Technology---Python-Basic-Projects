import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("\n\nSESSION 17 - HEART DISEASE DATASET")

#===============================================================
#===============================================================

print("\n\nQ1. Load the Heart Disease Dataset")

# Loading the dataset
df = pd.read_csv("heart.csv")

# Displaying first 10 rows
print("\nFirst 10 Rows:\n")
print(df.head(10))

# Displaying shape
print("\nShape of Dataset:")
print(df.shape)

# Displaying basic information
print("\nDataset Information:")
print(df.info())

#===============================================================
#===============================================================

print("\n\nQ2. Check Missing Values")

# Displaying total missing values in each column
print(df.isnull().sum())

#===============================================================
#===============================================================

print("\n\nQ3. Check Duplicate Rows")

# Counting duplicate rows
duplicates = df.duplicated().sum()

print("Duplicate Rows :", duplicates)

# Removing duplicate rows if found
if duplicates > 0:

    df = df.drop_duplicates()

    print("\nDuplicate rows removed successfully.")

else:

    print("\nNo duplicate rows found.")

# Displaying new shape
print("\nNew Shape of Dataset:")
print(df.shape)

#===============================================================
#===============================================================

print("\n\nQ4. Identify Invalid Values")

# Counting Cholesterol values equal to 0
chol_zero = (df["Cholesterol"] == 0).sum()

# Counting RestingBP values equal to 0
bp_zero = (df["RestingBP"] == 0).sum()

# Displaying counts
print("Rows with Cholesterol = 0 :", chol_zero)

print("Rows with RestingBP = 0 :", bp_zero)

print("\n\nQ5. Clean the Invalid Values")

# Displaying statistical summary before cleaning
print("\nBefore Cleaning:\n")
print(df[["Cholesterol", "RestingBP"]].describe())

# Calculating mean excluding zero values
chol_mean = df[df["Cholesterol"] != 0]["Cholesterol"].mean()

bp_mean = df[df["RestingBP"] != 0]["RestingBP"].mean()

# Replacing zero values with mean
df["Cholesterol"] = df["Cholesterol"].replace(0, chol_mean)

df["RestingBP"] = df["RestingBP"].replace(0, bp_mean)

# Rounding values to 2 decimal places
df["Cholesterol"] = df["Cholesterol"].round(2)

df["RestingBP"] = df["RestingBP"].round(2)

# Displaying statistical summary after cleaning
print("\nAfter Cleaning:\n")
print(df[["Cholesterol", "RestingBP"]].describe())

#===============================================================
#===============================================================

print("\n\nQ6. Histograms of Numerical Columns")

# Creating function for plotting histograms
def plot_histograms():

    # Creating figure
    plt.figure(figsize=(10,8))

    # Age
    plt.subplot(2,2,1)
    plt.hist(df["Age"], bins=10)
    plt.title("Age")

    # RestingBP
    plt.subplot(2,2,2)
    plt.hist(df["RestingBP"], bins=10)
    plt.title("RestingBP")

    # Cholesterol
    plt.subplot(2,2,3)
    plt.hist(df["Cholesterol"], bins=10)
    plt.title("Cholesterol")

    # MaxHR
    plt.subplot(2,2,4)
    plt.hist(df["MaxHR"], bins=10)
    plt.title("MaxHR")

    # Adjusting layout
    plt.tight_layout()

    # Displaying plots
    plt.show()

# Calling function
plot_histograms()

#===============================================================
#===============================================================

print("\n\nQ7. Numerical and Categorical Columns")

# Finding numerical columns
print("\nNumerical Columns:\n")

print(df.select_dtypes(include=np.number).columns)

# Finding categorical columns
print("\nCategorical Columns:\n")

print(df.select_dtypes(include="object").columns)

#===============================================================
#===============================================================

print("\n\nQ8. One-Hot Encoding")

# Performing One-Hot Encoding
df_encoded = pd.get_dummies(df)

# Displaying shape
print("\nShape of Encoded Dataset:")

print(df_encoded.shape)

# Displaying first 5 rows
print("\nFirst 5 Rows:\n")

print(df_encoded.head())

#===============================================================
#===============================================================

print("\n\nQ9. Final Dataset Information")

# Displaying final shape of encoded dataset
print("\nFinal Shape of Encoded Dataset:")
print(df_encoded.shape)

# Displaying all column names
print("\nColumn Names:\n")
print(df_encoded.columns)

#===============================================================
#===============================================================

print("\n\nQ10. Summary")

# Displaying summary of the analysis

print("""
1. Invalid Values Found:
   - Cholesterol values equal to 0.
   - RestingBP values equal to 0.
   - Both were replaced with the mean value of the respective column.

2. Importance of Handling Invalid Values:
   - Values like 0 are unrealistic and can affect the accuracy of data analysis
     and machine learning models.

3. Purpose of One-Hot Encoding:
   - It converts categorical (text) data into numerical (0 and 1) values
     so that machine learning algorithms can understand them.

4. Other Observations:
   - No missing values were found in the dataset.
   - Duplicate rows were removed (if present).
   - The dataset is now cleaned and ready for further analysis
     and machine learning.
""")

#===============================================================
#===============================================================