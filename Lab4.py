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
def genereaza_factura(nume_client, **produse):
    print("===== FACTURA =====")
    print(f"Client: {nume_client}")
    print("-------------------")

    total = 0

    for produs, pret in produse.items():
        print(f"{produs}: {pret} lei")
        total += pret

    print("-------------------")
    print(f"Total de plata: {total} lei")
    print("===================")



genereaza_factura(
    "Madalina",
    paine=5,
    lapte=7,
    oua=12
)


