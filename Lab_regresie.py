from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
x=np.array([[1],[2],[3],[4]])
y=np.array([5,6,7,8])
model=LinearRegression()
model.fit(x,y)
predictie=model.predict([[5]])
print(predictie)
diabetes=load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target
print(df.head())

print(df.describe())
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
df['bmi'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuția BMI')
plt.xlabel('BMI (Valoare scalată)')
plt.ylabel('Frecvență')
plt.show()

plt.scatter(df['age'], df['bmi'], c=df['target'], cmap='viridis')
plt.colorbar(label='Scor Diabet')
plt.xlabel('Vârstă')
plt.ylabel('BMI')
plt.title('Relația dintre Vârstă, BMI și Scorul Diabetului')
plt.show()