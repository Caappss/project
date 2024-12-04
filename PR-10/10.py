from random import randint
a=[]
n=int(input('Строчки: ')) #строки.
m=int(input('Столбцы: ')) #столбы.
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)

f=open('Lobanov_Aleksandr_Andreevich_UB-42_vvod.txt','w+')
for i in a:
    f.write(str(i), )
    f.write('\n')

f.close()
f = open('Lobanov_Aleksandr_Andreevich_UB-42_vvod.txt', 'r')
b=[]
for i in range(n):
    c=[]
    for j in range(m):
        b.append(randint(1,100))
    b.append(c)

max1=0
min1=1
for i in a:
    min1=i.index(min(i))
    max1=i.index(max(i))
    i[max1],i[0]=i[0],i[max1]
    i[min1],i[-1]=i[-1],i[min1] # обмен 2-ух переменных через временный кортеж.

f=open('Lobanov_Aleksandr_Andreevich_UB-42_vivod.txt','w+')
for i in a:
    f.write(str(i), )
    f.write('\n')

f.close()