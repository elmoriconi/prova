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

def mosse_tartaruga(quadrati, x, pioggia, stamina):
    if 1 <= x <= 5 and stamina >= 5: # passo veloce
        quadrati += 3
        stamina -= 5
    elif 6 <= x <= 7 and stamina >= 10: # scivolata
        if quadrati <= 6:
            quadrati = 1
        else:
            quadrati -= 6
        stamina -= 10
    elif 8 <= x <= 10 and stamina >= 3: # passo lento
        quadrati += 1
        stamina -= 3
    else:
        stamina += 10
    if pioggia:
        if quadrati > 1:
            quadrati -= 1
    return quadrati, stamina

def mosse_lepre(quadrati, x, pioggia, stamina):
    if 1 <= x <= 2: # riposo
        if stamina == 100:
            quadrati == quadrati
        else:
            quadrati == quadrati
            stamina += 10
    elif 3 <= x <= 4 and stamina >= 15: #grande balzo
        quadrati += 9
        stamina -= 15
    elif x == 5 and stamina >= 20: # grande scivolata
        if quadrati <= 12:
            quadrati == 1
        else:
            quadrati -= 12
        stamina -= 20
    elif 6 <= x <= 8 and stamina >= 5: # piccolo balzo
        quadrati += 1
        stamina -= 5
    elif 9 <= x <= 10 and stamina >= 8: # piccola scivolata
        quadrati -= 2
        stamina -= 8
    else:
        stamina += 10
    if pioggia:
        if quadrati > 1:
            quadrati -= 2
    return quadrati, stamina


print("BANG !!!!! AND THEY'RE OFF !!!!!")
lepre = 1
tartaruga = 1
pioggia: bool = False
secondi = 0
stamina_lepre = 100
stamina_tartaruga = 100
while lepre < 70 or tartaruga < 70:
    secondi += 1
    if secondi % 10 == 0:
        pioggia = not pioggia
    lepre, stamina_lepre = mosse_lepre(lepre, random.randint(1, 10), pioggia, stamina_lepre)
    tartaruga, stamina_tartaruga = mosse_tartaruga(tartaruga, random.randint(1, 10), pioggia, stamina_tartaruga)
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