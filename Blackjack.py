from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))
for carta,valor in cartas.items():
  print("la carta {} vale {} puntos".format(carta, valor))

lista_cartas = list(cartas)
print("\n")



print("Ha seleccionado",end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta,end=" ")
carta = choice(lista_cartas)
print(carta,end=" ")
score += cartas[carta]
print("La puntuacción es de:",score)
main_banca = sample(lista_cartas,2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {} su score es {}".format(main_banca[0],main_banca[1],score_banca))
puntuacion = cartas[carta]
a = score + puntuacion
def otra_carta(otra):
  otra=int(input("presiona 9 para pedir otra carta:"))
  if otra == 9:
    print("La nueva carta es:",end=" ")
    otra = choice(lista_cartas)
    print(carta,end=" ")
    puntuacion = cartas[otra]
    puntuacion += cartas[otra]
  return("La puntuación es",a)


if score > score_banca:
  print("Enhorabuena has ganado a la banca")
else:
  print(otra_carta(carta))
  if a > 21:
    print("Te has pasado la banca gana")
  elif a == 21:
    print("¡¡¡BLACKJACK!!!")
  elif a > score_banca:
    print("Enhorabuena has ganado a la banca")
  elif a < score_banca:
    print("Has perdido la banca ha ganado")
  
  else:
    print("empate")
