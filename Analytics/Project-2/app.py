# =====================
# 1. LOAD & CLEAN DATA
# =====================
'''Scenario 1: Data Loading & Preprocessing 
You are given the ign.csv dataset containing game reviews. 

Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows (head()) 
○ Last 5 rows (tail()) 
○ Shape of dataset 
3. Remove the unnecessary column: 
○ "Unnamed: 0" (index column) 
4. Check for missing values in: 
○ score, genre, platform 
5. Handle missing values: 
○ Fill numeric column score with mean 
○ Fill categorical column genre with mode 
6. Ensure correct data types: 
○ score → float 
○ release_year, release_month, release_day → integer# Import libraries'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\This PC\OneDrive\Desktop\PythonTasks\Analytics\Project-2\ign.csv")

print(df.head())

# Remove unwanted column
if "Unnamed: 0" in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

# Fill missing values
df['score'] = df['score'].fillna(df['score'].mean())
df['genre'] = df['genre'].fillna(df['genre'].mode()[0])

# Fix data types
df['score'] = df['score'].astype(float)
df['release_year'] = df['release_year'].astype(int)
print(df.tail())
print("Data Loaded Successfully\n")
# =====================
# 2. LINE GRAPH (TREND)
# =====================
'''Scenario 2: Line Graph (Score Trend) + Save 
You want to analyze how game scores change over time. 

Tasks: 
1. Group data by release_year. 
2. Calculate average score per year using Pandas. 
3. Convert results into NumPy arrays. 
4. Plot a line graph: 
○ X-axis → release_year 
○ Y-axis → average score 
5. Add: 
○ Title: "Average Game Score Over Years" 
○ Axis labels 
6. Save the graph: plt.savefig("avg_score_trend.png")'''

yearly = df.groupby('release_year')['score'].mean()

plt.figure()
plt.plot(yearly.index, yearly.values)
plt.title("Average Score Over Years")
plt.xlabel("Year")
plt.ylabel("Score")
plt.savefig("trend.png")
plt.show()
# =====================
# 3. BAR CHART
# =====================
'''Scenario 3: Filtering + Bar Chart + Save 
You want to compare top platforms. 

Tasks: 
1. Filter dataset where: 
○ score > 7 
2. Count number of high-rated games per platform. 
3. Select top 10 platforms using Pandas. 
4. Convert data into NumPy arrays. 
5. Plot a bar chart: 
○ X-axis → platform 
○ Y-axis → count of games 
6. Rotate x-axis labels for readability. 
Save the graph: plt.savefig("top_platforms_bar.png")'''

top_platforms = df[df['score'] > 7]['platform'].value_counts().head(10)

plt.figure()
plt.bar(top_platforms.index, top_platforms.values)
plt.xticks(rotation=45)
plt.title("Top Platforms")
plt.savefig("platforms.png")
plt.show() 
# =====================
# 4. PIE CHART
# =====================
'''Scenario 4: Aggregation + Pie Chart + Save 
You want to analyze genre distribution. 

Tasks: 
1. Count the number of games per genre. 
2. Select top 5 genres using Pandas. 
3. Prepare labels and values. 
4. Plot a pie chart: 
○ Labels → genre 
○ Values → count 
5. Add percentage labels (autopct). 
Save the graph: plt.savefig("genre_distribution.png")'''

top_genres = df['genre'].value_counts().head(5)
plt.figure()
plt.pie(top_genres.values, labels=top_genres.index, autopct='%1.1f%%')
plt.title("Top Genres")
plt.savefig("genres.png")
plt.show()
# =====================
# 5. ADVANCED (BASIC)
# ===================== 
'''Scenario 5: Advanced Analysis + Multiple Graphs 
You are asked to perform a detailed analysis of review patterns. 

Part 1: Feature Engineering 
1. Create a new column: 
○ score_category: 
■ score >= 9 → "Excellent" 
■ 7 <= score < 9 → "Good" 
■ < 7 → "Average" 
2. Convert editors_choice: 
○ Y → 1, N → 0 

Part 2: NumPy Analysis 
3. Use NumPy to: 
○ Calculate yearly score growth using np.diff() on average yearly scores 

Part 3: Visualizations 

Line Graph 
4. Plot trend of: 
○ Average score per release_year 

Stacked Bar Chart 
5. Show count of: 
○ score_category per release_year 

Histogram 
6. Plot distribution of: 
○ score 

Part 4: Save All Graphs 
plt.savefig("score_trend.png") 
plt.savefig("score_category_stacked.png") 
plt.savefig("score_distribution.png") 

Part 5: Insights 
Identify: 
● Which years had highest scores 
● Whether high scores increased over time 
● If editors_choice correlates with high scores'''

# Create score category
df['score_category'] = df['score'].apply(
lambda x: "Excellent" if x >= 9 else ("Good" if x >= 7 else "Average")
)
# Convert editors choice
df['editors_choice'] = df['editors_choice'].map({'Y': 1, 'N': 0}) 
# Growth using numpy
growth = np.diff(yearly.values)
print("Score Growth:", growth) 
# Histogram
plt.figure()
plt.hist(df['score'])
plt.title("Score Distribution")
plt.savefig("hist.png")
plt.show()
# Insight
print("\nAverage score by Editors Choice:")
