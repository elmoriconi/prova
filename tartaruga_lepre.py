import random

def visualizza_posizione(lepre, tartaruga):
    quadrati: list[int] = []
    for x in range(1, 71):
        quadrati.append("_")
    if lepre != tartaruga:
        quadrati[lepre] = "H"
        quadrati[tartaruga] = "T"
    else:
        quadrati[lepre] = "OUCH!!!"
    return(quadrati)

def mosse_tartaruga(quadrati, x):
    if 1 <= x <= 5: # passo veloce
        quadrati += 3
    elif 6 <= x <= 7: # scivolata
        if quadrati <= 6:
            quadrati = 1
        else:
            quadrati -= 6
    elif 8 <= x <= 10: # passo lento
        quadrati += 1
    return quadrati

def mosse_lepre(quadrati, x):
    if 1 <= x <= 2: # riposo
        quadrati == quadrati
    elif 3 <= x <= 4: #grande balzo
        quadrati += 9
    elif x == 5: # grande scivolata
        if quadrati <= 12:
            quadrati == 1
        else:
            quadrati -= 12
    elif 6 <= x <= 8: # piccolo balzo
        quadrati += 1
    elif 9 <= x <= 10: # piccola scivolata
        quadrati -= 2
    return quadrati


print("BANG !!!!! AND THEY'RE OFF !!!!!")
lepre = 1
tartaruga = 1
while lepre < 70 or tartaruga < 70:
    lepre = mosse_lepre(lepre, random.randint(1, 10))
    tartaruga = mosse_tartaruga(tartaruga, random.randint(1, 10))
    if lepre >= 70:
        print("HARE WINS || YUCH!!!")
        break
    elif tartaruga >= 70:
        print("TORTOISE WINS! || VAY!!!")
        break
    elif lepre >= 70 and tartaruga >= 70:
        print("IT'S A TIE.")
    else: 
        print(visualizza_posizione(lepre, tartaruga))
    