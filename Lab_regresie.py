from sklefrom sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.datasets import load_diabetes
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Creare model y = x+4
x = np.array([[1],[2],[3],[4]])
y = np.array([5,6,7,8])
model = LinearRegression()
model.fit(x,y)   # modelul este antrenat pe datele x si y
predictie = model.predict([[5]])
print(predictie)

# Exercitiul 1
diabetes = load_diabetes()
# Exercitiul 2, 3
df = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)
df['target'] = diabetes.target
print(df.head())

# Exercitiul 4
print(df.describe())  #statistici

# Exercitiul 5
plt.figure(figsize=(3,6))
plt.hist(df['bmi'], bins = 20)
plt.title("Histograma BMI")
plt.xlabel("BMI")
plt.ylabel("Frecventa")
plt.show()

# Exercitiul 6
plt.figure(figsize=(8,6))
plt.scatter(df['bmi'], df['age'], c = df['target'],  cmap = 'coolwarm')
plt.title("Scatter Plot")
plt.xlabel("BMI")
plt.ylabel("Varsta")
plt.colorbar(label = 'Target')
plt.show()
plt.close()
# Exercitiul 7

#a
X = df[['bmi']]        # input  - coloana bmi (2D)
y = df['target']       # target - scorul diabetului

#b
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#c
model = LinearRegression()
model.fit(X_train, y_train)

print(f"Coeficient (panta m):   {model.coef_[0]:.2f}")
print(f"Intercept (n):            {model.intercept_:.2f}")
y_pred = model.predict(X_test)

#d
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color="steelblue", alpha=0.6, label="Date testare")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Linie regresie")
plt.xlabel("BMI")
plt.ylabel("Scor diabet")
plt.title("Regresie Liniara Simpla - BMI vs Scor Diabet")
plt.legend()
plt.show()

#e
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"\nMSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")

# Exercitiul 8
#a
X2 = df[['bmi', 'bp']]
y = df['target']

#b
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(X2_train, y2_train)

#c
print("Coeficienti:")
for feature, coef in zip(X2.columns, model2.coef_):
    print(f"  {feature}: {coef:.2f}")
print(f"Intercept: {model2.intercept_:.2f}")

#d
y2_pred = model2.predict(X2_test)
r2 = model2.score(X2_test, y2_test)
print(f"\nScorul R^2: {r2:.4f}")arn.linear_model import LinearRegression


