import sys

def najmniejsza_liczba(a1, a2, a3):
	t=[]
	t.append(a1)
	t.append(a2)
	t.append(a3)
	t.sort()
	r=100*int(t[0])+10*int(t[1])+int(t[2])
	return r

for line in sys.stdin:
	print(line)
	a1,a2,a3=line.split(',')
	print(najmniejsza_liczba(a1, a2, a3))