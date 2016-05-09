import csv
from random import shuffle, choice
entries = {}
with open('/home/staffcreativa-luhego/Desktop/concursos_intersectados.csv', 'rb') as inputfile:
        reader = csv.reader(inputfile, delimiter=',')
        print 'reader', reader
        for row in reader:            
            key=row[0].zfill(8)
            entries[key] = 0

with open('/home/staffcreativa-luhego/Desktop/Concurso_cantidades.csv', 'rb') as inputfile2:
    reader2 = csv.reader(inputfile2, delimiter=',')
    contador = 0
    for row in reader2:
        if row[0] in entries.keys():  
            contador += 1          
            print 'row',row[0], row[5]
            entries[row[0]] = entries[row[0]] + int(row[5])
print 'entries', entries
print 'contador', contador

def ganador():
    lista_sorteo = []
    for key in entries.keys():
        for i in range(entries[key]):
            lista_sorteo.append(key)
    print lista_sorteo
    print 'lista count', len(lista_sorteo)
    shuffle(lista_sorteo)
    winner = choice(lista_sorteo)
    return winner
print ganador()