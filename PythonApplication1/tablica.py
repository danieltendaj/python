tablica=[]
for i in range(3):
	w=""
	for j in range(3):
		w=w+str(j)+" "
	tablica.append(w.split())
print(tablica)
for k in tablica:
	print(k)
	p=k[2]
	k[2]=k[1]
	k[1]=k[0]
	k[0]=p
print(tablica)	
