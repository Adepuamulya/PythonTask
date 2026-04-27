# ===============================================================================
  # 🟢 SCENARIO 1: Data Loading & Cleaning (🟢 Easy)
# ===============================================================================
'''�
�
Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows 
○ Column names 
3. Check for missing values in: 
○ Height 
○ Region 
4. Fill missing values: 
○ Height → use mean 
○ Region → use mode 
5. Convert Height column to numeric if required.'''

import pandas as pd

# ------------------------------
# STEP 1: LOAD DATASET
# ------------------------------
df = pd.read_csv("scottish_hills (1).csv")

# ------------------------------
# STEP 2: CONVERT HEIGHT (safety)
# ------------------------------
df["Height"] = pd.to_numeric(df["Height"], errors='coerce')

# ------------------------------
# STEP 3: CREATE REGION COLUMN
# ------------------------------
lat_mid = df["Latitude"].median()
lon_mid = df["Longitude"].median()

def assign_region(row):
    lat = row["Latitude"]
    lon = row["Longitude"]
    
    if lat >= lat_mid and lon >= lon_mid:
        return "North-East"
    elif lat >= lat_mid and lon < lon_mid:
        return "North-West"
    elif lat < lat_mid and lon >= lon_mid:
        return "South-East"
    else:
        return "South-West"

df["Region"] = df.apply(assign_region, axis=1)

# ------------------------------
# STEP 4: HANDLE MISSING VALUES
# ------------------------------
# Fill Height with mean
df["Height"].fillna(df["Height"].mean(), inplace=True)

# Fill Region with mode
df["Region"].fillna(df["Region"].mode()[0], inplace=True)

# ------------------------------
# STEP 5: OUTPUT
# ------------------------------
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# ===============================================================================
  # 🟢 SCENARIO 2: Line Graph (Score Trend) + Save (🟢 Easy)
# ===============================================================================
'''You want to see how heights vary. 
�
�
Tasks: 
1. Select: 
○ Hill Name 
○ Height 
2. Take first 10 rows only. 
3. Convert Height into a NumPy array. 
4. Plot a line graph: 
○ X-axis → index (0–9) 
○ Y-axis → Height 
5. Add title and labels. 
Save the graph: plt.savefig("hill_heights_line.png")'''
import numpy as np
import matplotlib.pyplot as plt

# 1. Select required columns
data = df[['Hill Name', 'Height']]

# 2. Take first 10 rows
data_10 = data.head(10)

# 3. Convert Height to NumPy array
height_array = np.array(data_10['Height'])

# 4. Plot line graph
plt.figure()
plt.plot(range(10), height_array, marker='o')

# 5. Add title and labels
plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index (0–9)")
plt.ylabel("Height")

# Save the graph
plt.savefig("hill_heights_line.png")

# Show plot
plt.show()

# ===============================================================================
  # 🟢 SCENARIO 3: Filtering + Bar Chart + Save
# ===============================================================================
'''You want to analyze tall hills. 
�
�
Tasks: 
1. Filter hills where: 
○ Height > 900 
2. Count number of hills per Region. 
3. Select top regions. 
4. Convert results to NumPy arrays. 
5. Plot a bar chart: 
○ X-axis → Region 
○ Y-axis → count 
6. Rotate labels for clarity. 
Save graph: plt.savefig("tall_hills_bar.png") '''
import os
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("scottish_hills (1).csv")

# Clean column names
df.columns = df.columns.str.strip()

# Filter tall hills
tall_hills = df[df["Height"] > 900]

# Sort and take top 10 tallest hills
top_hills = tall_hills.sort_values(by="Height", ascending=False).head(10)

# Prepare data
x = top_hills["Hill Name"]
y = top_hills["Height"]

# Create folder
os.makedirs("graph", exist_ok=True)

# Plot
plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.xlabel("Hill Name")
plt.ylabel("Height (m)")
plt.title("Top 10 Tallest Hills")
plt.xticks(rotation=45)
plt.tight_layout()

# Save and show
plt.savefig("graph/top_tall_hills.png")
plt.show()
# ===============================================================================
  # 🟢 SCENARIO 4: Pie Chart (Region Distribution) + Save (🟡 Medium)
# ===============================================================================
'''You want to see the distribution of hills. 
�
�
Tasks: 
1. Count the number of hills per Region. 
2. Select top 5 regions. 
3. Prepare labels and values. 
4. Plot a pie chart. 
5. Add percentage labels. 
Save graph: plt.savefig("region_distribution.png")'''
# ------------------------------
# SCENARIO 4: PIE CHART (CORRECT)
# ------------------------------
def height_category(h):
    if h >= 1000:
        return "Very High"
    elif h >= 800:
        return "High"
    else:
        return "Moderate"

df["Height_Category"] = df["Height"].apply(height_category)
# 1. Count hills per Height Category
category_counts = df["Height_Category"].value_counts()

# 2. Select top 5 categories (optional here but kept same structure)
top_categories = category_counts.head(5)

# 3. Prepare labels and values
labels = top_categories.index
values = top_categories.values

# 4. Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

# 5. Title
plt.title("Distribution of Hills by Height Category")

# Save graph
plt.savefig("category_distribution.png")

# Show plot
plt.show()
#=================================================================================================================================
  #🔴 SCENARIO 5: Advanced Analysis + Multiple Graphs (🔴 Hard)
#=================================================================================================================================
'''�� Part 1: Feature Creation
1. Create a new column:
○ Height Category:
■ Height >= 1000 → "Very High"
■ 800–999 → "High"
■ < 800 → "Moderate"
�� Part 2: NumPy Usage
2. Convert Height column to NumPy array.
Calculate height differences using:
np.diff()
�� Part 3: Visualizations
�� Line Graph
4. Plot height trend for all hills.
�� Stacked Bar Chart
5. Show count of Height Category per Region.
�� Histogram
6. Plot distribution of Height.
�� Part 4: Save All Graphs
plt.savefig("height_trend.png")
plt.savefig("height_category_stacked.png")
plt.savefig("height_histogram.png")
�� Part 5: Insights
● Which region has tallest hills
● Which category is most common
● Distribution pattern of heights'''

# ------------------------------
# SCENARIO 5: ADVANCED ANALYSIS
# ------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("scottish_hills (1).csv")
df.columns = df.columns.str.strip()

# ------------------------------
# PART 1: FEATURE CREATION
# ------------------------------
def height_category(h):
    if h >= 1000:
        return "Very High"
    elif h >= 800:
        return "High"
    else:
        return "Moderate"

df["Height_Category"] = df["Height"].apply(height_category)

# ------------------------------
# PART 2: NUMPY USAGE
# ------------------------------
height_array = np.array(df["Height"])

# Calculate differences
height_diff = np.diff(height_array)

print("\nFirst 10 Height Differences:")
print(height_diff[:10])

# ------------------------------
# CREATE FOLDER FOR SAVING GRAPHS
# ------------------------------
os.makedirs("graphs", exist_ok=True)

# ------------------------------
# PART 3: VISUALIZATIONS
# ------------------------------

# 🔹 1. Line Graph (Height Trend)
plt.figure()
plt.plot(range(len(height_array)), height_array)
plt.title("Height Trend of All Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.savefig("graphs/height_trend.png")
plt.show()

# 🔹 2. Stacked Bar Chart (Category only - no Region column)
category_counts = df["Height_Category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.title("Height Category Distribution")
plt.xlabel("Height Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("graphs/height_category_stacked.png")
plt.show()

# 🔹 3. Histogram (Height Distribution)
plt.figure()
plt.hist(df["Height"], bins=10)
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.savefig("graphs/height_histogram.png")
plt.show()


# 🔹 3. Histogram (Height Distribution)
plt.figure()
plt.hist(df["Height"], bins=10)
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.savefig("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_3/pictorial_analysis/height_histogram.png")
plt.show()