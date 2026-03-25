from selectors import SelectSelector
#exercitiul 1
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]

for x in picture:
          for y in x:
              if y==1:
                  print('*', end='')
              else:
                  print(' ', end='')
          print()

#exercitiul2
nota=int(input("Nota: "))
print("Nota: ", nota)
if nota<=10 and nota>=9:
    print("Excelent")
elif nota>=7 and nota<=8:
    print("Bine")
elif nota>=5 and nota<=6:
    print ("Suficient")
else:
    print("Reexaminare")

#exercitiul3
import random
numar=random.randint(1,50)
nr=int(input("nr:"))
print("nr:", nr)
c=1
while nr!=numar:
    if nr>numar:
        c=c+1
        print("numarul este mai mic ")
    else:
        c=c+1
        print("numarul este mai mare ")
        nr=int(input("nr:"))
        print("nr:", nr)
print("felicitari, ai ghicit din ", c, "incercari")
print()
print(numar)





