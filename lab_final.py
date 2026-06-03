from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

x = iris.data
y = iris.target

print("Forma setului de date:", x.shape)

print("\nDenumirile atributelor:")
print(iris.feature_names)

print("\nClasele:")
print(iris.target_names)

# 2.1.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 2.2.
print(f"\nForma subsetului de antrenare (x_train): {x_train.shape}")
print(f"Forma subsetului de testare (x_test): {x_test.shape}")
print(f"Forma etichetelor de antrenare (y_train): {y_train.shape}")
print(f"Forma etichetelor de testare (y_test): {y_test.shape}")

print(x)
print(y)
from sklearn.preprocessing import StandardScaler

# --- 3.1.

scaler = StandardScaler()


x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# --- 3.2.
print("\n" + "="*30)
print("COMPARAȚIE DATE (Primele 3 rânduri)")
print("="*30)

print("\nÎnainte de scalare (x_train):")
print(x_train[:3])

print("\nDupă scalare (x_train_scaled):")
print(x_train_scaled[:3])

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# --- 4.1.

knn = KNeighborsClassifier(n_neighbors=3)

# --- 4.2.

knn.fit(x_train_scaled, y_train)


y_pred = knn.predict(x_test_scaled)


accuracy = accuracy_score(y_test, y_pred)

print(f"Acuratețea modelului KNN pe setul de testare este: {accuracy * 100:.2f}%")

import matplotlib.pyplot as plt


k_values = range(1, 16)
accuracies = []

# 5.1.
for k in k_values:
    model_knn = KNeighborsClassifier(n_neighbors=k)
    model_knn.fit(x_train_scaled, y_train)

    score = model_knn.score(x_test_scaled, y_test)
    accuracies.append(score)

# 5.2.
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, marker='o', linestyle='--', color='b')
plt.title('Influența valorii K asupra Acurateții')
plt.xlabel('Valoarea lui K')
plt.ylabel('Acuratețe')
plt.xticks(k_values)
plt.grid(True)
plt.show()

from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# 6.1.
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicție (Ce a crezut modelul)')
plt.ylabel('Realitate (Ce era de fapt)')
plt.title('Matricea de Confuzie')
plt.show()

# 6.2.
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print("\nRaport de Clasificare:")
print(report)

#7
import matplotlib.pyplot as plt

plt.scatter(X[:, 2], X[:, 3], c=y)
plt.title(" Distributia speciilor")

noua_floare=[[5.1, 3.5, 1.4, 0.2]]
noua_floare_scaled=scaler.transform(noua_floare)
rezultat=knn.predict(noua_floare_scaled)
print(f"Specia prezisa: {iris.target_names[rezultat[0]]}")