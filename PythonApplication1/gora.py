import sys
import math

mountain_max = 0
i_max = 0

print(mountain_max)
print(i_max)

a = [0, 3, 1, 5, 4, 6, 7, 9]
    

for i in range(8):

    if (mountain_max < a[i]):
        mountain_max = a[i]
        i_max = i

    print(i, a[i], mountain_max)
    input()    

print (i_max, mountain_max)
    
