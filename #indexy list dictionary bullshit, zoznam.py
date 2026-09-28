#indexy list dictionary bullshit, zoznamy, 
# list vzdy v [], a dictionary nemoze mat tu istu polozku viackrat [], ale po vypise {}. 
# dictionary vypis {10:7, 'a':3}
# su tam pismenka, musi byt string
def prevodnik(number:str)->int:
    prevod = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10,'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    suma=0
    index = 0
    
    for symbol in number.upper()[::-1]:
        suma += prevod[symbol]*16*index


        index +=1
    return suma


print(prevodnik('AA'))
#reversni za DU