# Simple Regression Algorithms Code
# Dataset: kc_house_data.csv

# Import Libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error


# Load Dataset
df = pd.read_csv("kc_house_data.csv")

# Show first 5 rows
print(df.head())


# Select simple input columns
X = df[["bedrooms", "bathrooms", "sqft_living", "floors"]]

# Target column (price)
y = df["price"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ------------------------------------------------
# 1. Linear Regression
# ------------------------------------------------
print("Linear Regression")

model1 = LinearRegression()
model1.fit(X_train, y_train)

pred1 = model1.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred1))


# ------------------------------------------------
# 2. Ridge Regression
# ------------------------------------------------
print("\nRidge Regression")

model2 = Ridge()
model2.fit(X_train, y_train)

pred2 = model2.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred2))


# ------------------------------------------------
# 3. Decision Tree Regressor
# ------------------------------------------------
print("\nDecision Tree Regressor")

model3 = DecisionTreeRegressor()
model3.fit(X_train, y_train)

pred3 = model3.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred3))


# ------------------------------------------------
# 4. Random Forest Regressor
# ------------------------------------------------
print("\nRandom Forest Regressor")

model4 = RandomForestRegressor()
model4.fit(X_train, y_train)

pred4 = model4.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred4))


# ------------------------------------------------
# 5. Support Vector Regressor
# ------------------------------------------------
print("\nSupport Vector Regressor")

model5 = SVR()
model5.fit(X_train, y_train)

pred5 = model5.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred5))


# ------------------------------------------------
# 6. KNN Regressor
# ------------------------------------------------
print("\nKNN Regressor")

model6 = KNeighborsRegressor()
model6.fit(X_train, y_train)

pred6 = model6.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred6))


# ------------------------------------------------
# 7. Gradient Boosting Regressor
# ------------------------------------------------
print("\nGradient Boosting Regressor")

model7 = GradientBoostingRegressor()
model7.fit(X_train, y_train)

pred7 = model7.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred7))

#--------------------------------------------------
#8. Implementing ElasticNet Regression
#--------------------------------------------------

from sklearn.linear_model import ElasticNet
model = ElasticNet()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("ElasticNet Performance:")
print("MAE:",mean_absolute_error(y_test, y_pred))


#------------------------------------------------
#9. Implementing AdaBoost Regressor
#------------------------------------------------

from sklearn.ensemble import AdaBoostRegressor
model = AdaBoostRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("AdaBoostRegressor Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))


#--------------------------------------------------
#10. Implementing Extra Trees Regressor
#--------------------------------------------------

from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
print(model)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('-'*80)
print("ExtraTreeRegressor Performance:")
print("MAE:",mean_absolute_error(y_test, y_pred))