import os

end_number = str(input('prosze podac koncowy numer: '))
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

    END = '('+end_number+').dxf'
    z = lista[i][0:-4]
    print(lista[i][0:-4],end= END)
    print('\n**********')
    nowa_lista.append(z+END)

print(nowa_lista)


'''JESZCZE POPRAWIĆ rename aby dodać (1), (2) do każdego elementu)'''
#rename function
for i in range(len(lista)):
    os.rename(lista[i],nowa_lista[i])


    

input('\nWcisnij enter aby kontynuowac')
