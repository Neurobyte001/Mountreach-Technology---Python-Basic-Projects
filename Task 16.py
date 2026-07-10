import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#===============================================================
#===============================================================

print("\n\nQ1. Load the Insurance Dataset")

# Loading the dataset
df = pd.read_csv("insurance - insurance.csv")

# Displaying first 10 rows
print(df.head(10))

#===============================================================
#===============================================================

print("\n\nQ2. Basic Information of Dataset")

# Displaying shape
print("\nShape of Dataset:")
print(df.shape)

# Displaying information
print("\nDataset Information:")
print(df.info())

# Displaying statistical summary
print("\nStatistical Summary:")
print(df.describe())

#===============================================================
#===============================================================

print("\n\nQ3. Checking Missing Values")

# Displaying null values in each column
print(df.isnull().sum())

#===============================================================
#===============================================================

print("\n\nQ4. Identify Numerical and Categorical Columns")

# Finding numerical columns
print("\nNumerical Columns:")
print(df.select_dtypes(include=np.number).columns)

# Finding categorical columns
print("\nCategorical Columns:")
print(df.select_dtypes(include="object").columns)

#===============================================================
#===============================================================

print("\n\nQ5. Distribution Plots")

# Distribution plot for Age
plt.figure(figsize=(6,4))
sns.histplot(df["age"], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Distribution plot for BMI
plt.figure(figsize=(6,4))
sns.histplot(df["bmi"], kde=True)
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()

# Distribution plot for Children
plt.figure(figsize=(6,4))
sns.histplot(df["children"], kde=True)
plt.title("Children Distribution")
plt.xlabel("Children")
plt.ylabel("Frequency")
plt.show()

# Distribution plot for Charges
plt.figure(figsize=(6,4))
sns.histplot(df["charges"], kde=True)
plt.title("Insurance Charges Distribution")
plt.xlabel("Charges")
plt.ylabel("Frequency")
plt.show()

#===============================================================
#===============================================================

print("\n\nQ6. Count Plots for Categorical Columns")

# Count plot for Sex
plt.figure(figsize=(6,4))
sns.countplot(x=df["sex"])
plt.title("Gender Count")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.show()

# Count plot for Smoker
plt.figure(figsize=(6,4))
sns.countplot(x=df["smoker"])
plt.title("Smoker Count")
plt.xlabel("Smoker")
plt.ylabel("Count")
plt.show()

# Count plot for Region
plt.figure(figsize=(6,4))
sns.countplot(x=df["region"])
plt.title("Region Count")
plt.xlabel("Region")
plt.ylabel("Count")
plt.show()

#===============================================================
#===============================================================

print("\n\nQ7. Correlation Heatmap")

# Finding correlation between numerical columns
corr = df.corr(numeric_only=True)

# Creating heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.show()

#===============================================================
#===============================================================

print("\n\nQ8. Analysis on Charges Column")

# Displaying average charges
print("Average Charges :", df["charges"].mean())

# Displaying maximum charges
print("Maximum Charges :", df["charges"].max())

# Displaying minimum charges
print("Minimum Charges :", df["charges"].min())

# Comparing smoker and non-smoker charges
print("\nAverage Charges based on Smoking Status:\n")

print(df.groupby("smoker")["charges"].mean())

#===============================================================
#===============================================================

print("\n\nQ9. Boxplots")

# Boxplot for Charges vs Smoker
plt.figure(figsize=(6,4))

sns.boxplot(x="smoker", y="charges", data=df)

plt.title("Charges according to Smoking Status")

plt.xlabel("Smoker")

plt.ylabel("Charges")

plt.show()

# Boxplot for Charges vs Sex
plt.figure(figsize=(6,4))

sns.boxplot(x="sex", y="charges", data=df)

plt.title("Charges according to Gender")

plt.xlabel("Sex")

plt.ylabel("Charges")

plt.show()

#===============================================================
#===============================================================

print("\n\nQ10. Mini Project - Analysis Summary")

# Calculating average age
avg_age = df["age"].mean()

# Calculating average BMI
avg_bmi = df["bmi"].mean()

# Finding region with highest customers
top_region = df["region"].value_counts().idxmax()

# Printing summary
print(f"Average Age : {avg_age:.2f}")

print(f"Average BMI : {avg_bmi:.2f}")

print("\nAverage Charges based on Smoking Status:")

print(df.groupby("smoker")["charges"].mean())

print(f"\nRegion with Highest Customers : {top_region}")

print("\nObservations:")

print("1. Smokers have much higher insurance charges than non-smokers.")

print("2. Insurance charges contain several high-value outliers.")

print("3. Age and BMI have a positive relationship with insurance charges.")

print("4. The dataset contains no missing values.")

print("5. Numerical variables show different distributions.")

#===============================================================
#===============================================================

