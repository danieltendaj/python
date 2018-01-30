
wysokosc = input("Podaj liczbę bloków ")
spacjator = int(wysokosc)-1

dodawacz = 1
 
for i in range(int(wysokosc)):
    for j in range (spacjator):
        print ( end = ' ')
    for k in range (dodawacz):          
        print (dodawacz, end = ' ')
    print (" ")
    dodawacz+=1
    spacjator-=1