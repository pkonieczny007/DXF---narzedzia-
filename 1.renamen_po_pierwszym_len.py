import os

#listowanie plików dxf
lista = []

for filename in os.listdir():
    if filename.endswith('.dxf'):
        with open(filename) as f: 
            print(filename)
            lista.append(filename)

#tworzenie nowej listy
nowa_lista = []

lista.sort(key = len)

for i,j in enumerate(lista,0):

    END = '('+str(i)+').dxf'
    z = lista[0][0:-4]
    print(lista[0][0:-4],end= END)
    print('\n**********')
    nowa_lista.append(z+END)

#głupie teksty
'''name = input('wcisnij enter aby kontynuowac!!')
print('oto lista :',lista)
print('\n\n*************\n\nmaking!!!!')
print(lista[0])
print('<---:\nOto element zero')

print('well done;;')
'''
#rename function
for i in range(len(lista)):
    os.rename(lista[i+1],nowa_lista[i+1])


#otwieranie folderu
'''   
path_open = r"D:\TECHNOLOGIA\2021\04_21 - 45552489\DXF"
path_open = os.path.realpath(path_open)
os.startfile(path_open)
'''

#użycie funkcji skanera

from scaner import scan

scan()
#input('\nWcisnij enter aby kontynuowac')
