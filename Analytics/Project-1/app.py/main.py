# =======================================================================================================
# 📊 Project Title: Railway Gauge Data Analysis
# =======================================================================================================

# 📦 1. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# =======================================================================================================
# 🟢 Scenario 1: Data Loading & Cleaning
# =======================================================================================================

df = pd.read_csv("railway_gauges.csv")

print(df.head())
print(df.columns)

# Fill missing values
df.fillna(0, inplace=True)

# Convert all columns except Year to numeric
cols = [col for col in df.columns if col != "Year"]
df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

print(df.dtypes)


# =======================================================================================================
# 🟢 Scenario 2: Line Graph
# =======================================================================================================

plt.plot(df["Year"], df["Total"], marker="o")
plt.xlabel("YEAR")
plt.ylabel("TOTAL")
plt.title("Total tracks over years")
plt.tight_layout()
plt.show()

print("Trend is increasing year by year but with some dips in later years")


# =======================================================================================================
# 🟡 Scenario 3: Bar Chart (After 2000)
# =======================================================================================================

# Convert year once
df["Year_in_int"] = df["Year"].astype(str).str[:4].astype(int)

fil_df = df[df["Year_in_int"] > 2000]

x = np.arange(len(fil_df))
width = 0.2

plt.style.use("ggplot")

plt.bar(x - width, fil_df["Broad Gauge"], width, label="Broad", color="grey")
plt.bar(x, fil_df["Metre Gauge"], width, label="Metre", color="blue")
plt.bar(x + width, fil_df["Narrow Gauge"], width, label="Narrow", color="green")

plt.xticks(x, fil_df["Year_in_int"])
plt.xlabel("Year")
plt.ylabel("three gauges")
plt.title("bar chart comparing all three gauges")
plt.legend()
plt.show()

print("Broad gauge dominented since 2000")


# =======================================================================================================
# 🟡 Scenario 4: Pie Chart
# =======================================================================================================

totals = df[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum()

plt.pie(
    totals,
    labels=["Broad Gauge", "Metre Gauge", "Narrow Gauge"],
    autopct="%1.1f%%",
    explode=(0.1, 0, 0),
    startangle=180
)

plt.title("percentage contribution")
plt.show()

print("Broad Gauge contributes the most to the total railway network among all gauge types.")


# =======================================================================================================
# 🔴 Scenario 5: Advanced Analysis
# =======================================================================================================

# Percentage columns
df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100

# Growth
df["Yearly_growth"] = np.insert(np.diff(df["Total"]), 0, 0)

print(df["Yearly_growth"])

# Line graph
plt.plot(df["Year_in_int"], df["Narrow Gauge"], label="Narrow Gauge", marker="o", color="grey")
plt.plot(df["Year_in_int"], df["Metre Gauge"], label="Metre Gauge", marker="o", color="green")
plt.plot(df["Year_in_int"], df["Broad Gauge"], label="Broad Gauge", marker="o", color="blue")

plt.xlabel("Year")
plt.ylabel("Gauges")
plt.legend()
plt.show()

# Stacked bar
plt.bar(df["Year_in_int"], df["Narrow Gauge"], label="Narrow Gauge", color="grey")
plt.bar(df["Year_in_int"], df["Metre Gauge"], bottom=df["Narrow Gauge"], label="Metre Gauge", color="green")
plt.bar(
    df["Year_in_int"],
    df["Broad Gauge"],
    bottom=df["Metre Gauge"] + df["Narrow Gauge"],
    label="Broad Gauge",
    color="blue"
)

plt.xlabel("Year")
plt.ylabel("Gauges")
plt.legend()
plt.show()

# Analysis
year_highest_growth = df.loc[df["Yearly_growth"].idxmax(), "Year_in_int"]
print(year_highest_growth)

print("Decline years:")
print(df.loc[df["Yearly_growth"] < 0, "Year_in_int"])

print("Yes, the railway system is clearly shifting toward a single dominant gauge that is Broad Gauge.")