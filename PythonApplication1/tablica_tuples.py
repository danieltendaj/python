tablica=[]
w=(0, 1, 2)
for i in range(3):
	tablica.append(w)
print(tablica)
lista=[]
for k in tablica:
	k0, k1, k2 = k
	k0, k1, k2 = k2, k0, k1
	k = k0, k1, k2
	lista.append(k)
print(lista)
