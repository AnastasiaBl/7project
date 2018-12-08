f_in=open('stock.txt','r')
f_out=open('order.txt','w')
stock=f_in.readlines()
vegetables = stock[0]
countveg = stock[1].split()
fruits = stock[2]
countfru = stock[3].split()
print("Склад: ",vegetables,fruits)
lcountveg=[]
lcountfru=[]
lcountveg1=[]
lcountfru1=[]
lveg=vegetables.split()
lfru=fruits.split()
for i in countveg:
    lcountveg.append(int(i))
    lcountveg1.append(int(i))
for i in countfru:
    lcountfru.append(int(i))
    lcountfru1.append(int(i))
choice = 'да'
while choice == 'да':
    order=input("Выберите наименование товара который вы хотите приобрести: ")
    for i in range(len(lveg)):
        if lveg[i] == order:
                    count = int(input("Сколько кг вы хотите приобрести? "))
                    while lcountveg[i]<count:
                        count=int(input("На складе нет такого кол-ва товара, выберите другой вес"+"(Допустимо: "+str(lcountveg[i])+"кг.):"))
                    lcountveg[i] -= count
        elif lfru[i] == order:
                    count = int(input("Сколько кг вы хотите приобрести? "))
                    while lcountfru[i]<count:
                        count=int(input("На складе нет такого кол-ва товара, выберите другой вес"+"(Допустимо: "+str(lcountfru[i])+"кг.):"))
                    lcountfru[i] -= count
    choice=input("Вы хотите продолжить формирование заказа? Напишите да или нет: ")
print('Овощи:', file= f_out)
for i in range(len(lveg)):
    lcountveg1[i]-=lcountveg[i]
    print(lveg[i],":",str(lcountveg1[i]),"кг.",file=f_out)
print("Фрукты", file=f_out)
for i in range(len(lfru)):
    lcountfru1[i]-=lcountfru[i]
    print(lfru[i], ":", str(lcountfru1[i]),"кг.", file=f_out)
f_in.close()
f_out.close()
ord = open('order.txt','r')
ord1 = ord.read()
print("Ваш заказ: \n",ord1)
ord.close()


