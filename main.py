a = input()
power_of_two = [2**i for i in range(10)]

hamming = []
i = 1
j = 1

#tablice aby przechowac pozycje bitow gdzie 1 oraz parity bits
ktore_1 = []
parity = []

while i <= len(a):
    if j in power_of_two:
        hamming.append( 0 )
        parity.append(j)
    else:  
        hamming.append(int(a[i-1]) )
        if int(a[i-1]) == 1:
            ktore_1.append(j)
        i+=1
    j+=1

print(hamming)
#xor aby wiedziec gdzie dac 1 na parity bits
res = 0
for k in ktore_1:
    res = res ^ k

#zamiania res na binary oraz ustawienie odpowiednich bitow
res = (bin(res).split('0b'))[-1]
l = 0
for i in res[::-1]:
    hamming[parity[l]-1] = int(i)
    l+=1


print(hamming)
