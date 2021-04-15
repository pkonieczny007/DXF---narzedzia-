import os

#word = str(input('prosze podac poczatkowy napis: '))
word = 'PAKS3_'
#listowanie plików dxf
lista = []

for filename in os.listdir():
    if filename.endswith('.dxf'):
        with open(filename) as f: 
            print(filename)
            lista.append(filename)

#tworzenie nowej listy
nowa_lista = []



for i,j in enumerate(lista,0):

    END = '.dxf'
    START = word
    z = lista[i][0:-4]
    print(lista[i][0:-4],end= END)
    print('\n**********')
    new= START + z + END
	
    nowa_lista.append(new)

print(nowa_lista)


'''JESZCZE POPRAWIĆ rename aby dodać (1), (2) do każdego elementu)'''
#rename function
for i in range(len(lista)):
    os.rename(lista[i],nowa_lista[i])


    

input('\nWcisnij enter aby kontynuowac')
