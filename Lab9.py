import pandas as pd

data=pd.read_csv('data.csv')

 #Ex1
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# print(data)

 #Ex2
# rezultat = data[data['Age'] > 40].head(10)
# print(rezultat)

#Ex3
# rezultat = data[(data['Overall'] >= 85) & (data['Age'] < 25)]
# print(rezultat)

#Ex4
# sortare = data.sort_values(by='Skill Moves', ascending=False)
# print(sortare)

#Ex5
# rezultat = data[data['Contract Valid Until'] =='2021']
# print(rezultat)

#Ex6
# print("Dimensiuni (rânduri, coloane):", data.shape)
# jucatori_unici = data['Name'].nunique()
# print("Număr jucători unici:", jucatori_unici)

#Ex7
# nationalitati = data['Nationality'].value_counts()
# print("Cea mai frecventă naționalitate este:", nationalitati.index[0])
# print("\nTop 5 naționalități:")
# print(nationalitati.head(5))

#Ex8
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv')
top_5_nat = data['Nationality'].value_counts().head(5)
plt.figure(figsize=(8, 8))
plt.pie(top_5_nat, labels=top_5_nat.index, autopct='%1.1f%%', startangle=140)
plt.title('Proporția jucătorilor pe naționalități (Top 5)')
plt.show()
print(top_5_nat)
