# lis =[1, 3, 5 , 6, 2]
# print(" The sum of the list element is: ", end ="")
# print (functools.reduce(lambda x, y: x + y, lis))
#
# def fibonacii(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacii(n-1)+fibonacii(n-2)
#
# result=fibonacii(4)
# print(result)

#exercitiul 1
# def obtine_alegere(jucator):
#     alegere = input(f"{jucator}, alege (piatra/hartie/foarfeca): ").lower()
#     while alegere not in ["piatra", "hartie", "foarfeca"]:
#         print("Alegere invalida! Incearca din nou.")
#         alegere = input(f"{jucator}, alege (piatra/hartie/foarfeca): ").lower()
#     return alegere
#
#
# def determina_castigator(a1, a2):
#     if a1 == a2:
#         return "egal"
#     elif (a1 == "piatra" and a2 == "foarfeca") or \
#          (a1 == "foarfeca" and a2 == "hartie") or \
#          (a1 == "hartie" and a2 == "piatra"):
#         return "jucator1"
#     else:
#         return "jucator2"
#
#
# def afiseaza_rezultat(rezultat):
#     if rezultat == "egal":
#         print("Este egalitate!")
#     elif rezultat == "jucator1":
#         print("Felicitari! Jucatorul 1 a castigat!")
#     else:
#         print("Felicitari! Jucatorul 2 a castigat!")
#
#
# def joaca():
#     while True:
#         alegere1 = obtine_alegere("Jucatorul 1")
#         alegere2 = obtine_alegere("Jucatorul 2")
#
#         rezultat = determina_castigator(alegere1, alegere2)
#         afiseaza_rezultat(rezultat)
#
#         din_nou = input("Doriti sa jucati din nou? (da/nu): ").lower()
#         if din_nou != "da":
#             print("Multumim pentru joc!")
#             break
#
#
#
# joaca()
#


#exercitiul 2
# def genereaza_factura(nume_client, **produse):
#     print("===== FACTURA =====")
#     print(f"Client: {nume_client}")
#     print("-------------------")
#
#     total = 0
#
#     for produs, pret in produse.items():
#         print(f"{produs}: {pret} lei")
#         total += pret
#
#     print("-------------------")
#     print(f"Total de plata: {total} lei")
#     print("===================")
#
#
#
# genereaza_factura(
#     "Madalina",
#     paine=5,
#     lapte=7,
#     oua=12
# )


#exercitiul 3
# def normalize_data(data):
#
#     if not data:
#         return []
#
#     min_val = min(data)
#     max_val = max(data)
#
#     if min_val == max_val:
#         return [0.0 for _ in data]
#
#     normalized = []
#     for x in data:
#         x_norm = (x - min_val) / (max_val - min_val)
#         normalized.append(x_norm)
#
#     return normalized
#
# data = [10, 20, 30, 40, 50]
# normalized_data = normalize_data(data)
#
# print(normalized_data)


#exercitiul 4
# square_list = lambda lst: [x**2 for x in lst]
#
# print(square_list([1, 2, 3]))

#exercitiul 5
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#
# sorted_a = sorted(a, key=lambda x: x[1])
#
# print(sorted_a)


#exercitiul 6
# def get_even_numbers(numbers):
#     return list(filter(lambda x: x % 2 == 0, numbers))
#
# def get_odd_numbers(numbers):
#     return list(filter(lambda x: x % 2 != 0, numbers))
#
#
# orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_list = get_even_numbers(orig_list)
# odd_list = get_odd_numbers(orig_list)
#
# print("Lista originala:", orig_list)
# print("Numere pare:", even_list)
# print("Numere impare:", odd_list)


#exercitiul 7
# def remove_none(prices):
#     return list(filter(lambda x: x is not None, prices))
#
# def apply_discount(prices):
#     return list(map(lambda x: x * 0.9, prices))
#
#
# prices = [100, 200, None, 50, None, 300]
#
# valid_prices = remove_none(prices)
# discounted_prices = apply_discount(valid_prices)
#
# print("Lista de preturi initiale:", prices)
# print("Fara None:", valid_prices)
# print("Cu reducerea de 10%:", discounted_prices)

#exercitiul 8
# from datetime import datetime
#
# dt = datetime(2004, 4, 1, 9, 3, 32, 744178)
#
#
# get_year = lambda x: x.year
# get_month = lambda x: x.month
# get_day = lambda x: x.day
# get_time = lambda x: x.time()
#
#
# print(dt)
# print(get_year(dt))
# print(get_month(dt))
# print(get_day(dt))
# print(get_time(dt))

#exercitiul 9
# def sum_lists(list1, list2):
#     return [a + b for a, b in zip(list1, list2)]
#
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
#
# result = sum_lists(list1, list2)
#
# print(result)

#exercitiul 10
# even_numbers = [x for x in range(0, 101) if x % 2 == 0]
#
# cubes = [x**3 for x in range(1, 11)]
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# common = [x for x in list1 if x in list2]
#
# print("Numerele pare (0-100):")
# print(even_numbers)
#
# print("\nCuburile primelor 10 numere:")
# print(cubes)
#
# print("\nElementele comune:")
# print(common)

#exercitiul 11

# even_set = {x for x in range(0, 20) if x % 2 == 0}
#
#
# text = "programare python"
# letters_set = {ch for ch in text if ch != " "}
#
# sentence = "Invatam programare in Python foarte usor"
# words_set = {word for word in sentence.split() if len(word) >= 5}
#
#
# print("Set numere pare:")
# print(even_set)
#
# print("\nLiterele distincte:")
# print(letters_set)
#
# print("\nCuvinte de minim 5 litere:")
# print(words_set)


#exercitiul 12

squares_dict = {x: x**2 for x in range(1, 11)}

text = "programare python"
letters_count = {ch: text.count(ch) for ch in text if ch != " "}

divisors_dict = {x: [i for i in range(1, x+1) if x % i == 0] for x in range(1, 11)}

print("Numerele și pătratele lor:")
print(squares_dict)

print("\nNumere apariții litere:")
print(letters_count)

print("\nNumerele și lista divizorilor:")
print(divisors_dict)

