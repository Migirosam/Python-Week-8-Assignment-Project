"""
COVID-19 Global Data Tracker
Author: Your Name
Description: Analyze COVID-19 cases, deaths, and vaccinations using Python.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 1: Load Data
# -------------------------------
print("Loading dataset...")
df = pd.read_csv("owid-covid-data.csv")

print("Preview of dataset:")
print(df.head())

# -------------------------------
# Step 2: Data Cleaning
# -------------------------------
print("\nCleaning dataset...")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Filter selected countries
countries = ["Kenya", "United States", "India"]
df_subset = df[df["location"].isin(countries)]

# Drop rows with no total_cases
df_subset = df_subset.dropna(subset=["total_cases"])

print(f"Filtered dataset includes {len(df_subset)} records.")

# -------------------------------
# Step 3: Exploratory Data Analysis
# -------------------------------
print("\nGenerating plots...")

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_subset[df_subset["location"] == country]
    plt.plot(country_data["date"], country_data["total_cases"], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# -------------------------------
# Step 4: Vaccination Progress
# -------------------------------
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_subset[df_subset["location"] == country]
    plt.plot(country_data["date"], country_data["total_vaccinations"], label=country)

plt.title("Vaccination Rollout Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# -------------------------------
# Step 5: Insights
# -------------------------------
print("\n--- Insights ---")
for country in countries:
    latest = df_subset[df_subset["location"] == country].sort_values("date").iloc[-1]
    total_cases = latest["total_cases"]
    total_deaths = latest["total_deaths"]
    death_rate = (total_deaths / total_cases) * 100 if total_cases > 0 else 0
    print(f"{country}: {total_cases:,.0f} cases, {total_deaths:,.0f} deaths, Death Rate: {death_rate:.2f}%")
