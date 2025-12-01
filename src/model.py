import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# 1️⃣ Load cleaned data
df = pd.read_csv("../data/cleaned/sales_data_cleaned.csv")

# 2️⃣ Feature engineering
# For simplicity, we predict Profit based on Sales and Quantity
X = df[['Sales', 'Quantity']]
y = df['Profit']

# 3️⃣ Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5️⃣ Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model trained successfully!")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# 6️⃣ Save model
with open("../model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl in project folder")
