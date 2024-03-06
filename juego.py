import random

from personaje import Personaje

class Juego:

  def __init__(self):
    self.personaje = None
    self.orco = Personaje("Orco")

  def iniciar_juego(self):
    nombre = input("Ingrese su nombre: ")
    self.personaje = Personaje(nombre)
    print(f"**Bienvenido al juego {self.personaje.nombre}!**")

    print(f"**Estado actual:**")
    print(self.personaje.get_estado())

    probabilidad_ganar = self.calcular_probabilidad_ganar()

    print(f"**Ha aparecido un orco!**")
    print(f"Tu probabilidad de ganarle es de {probabilidad_ganar:.2%}")
    print("En caso de ganarle, recibirás 50 puntos de experiencia y el orco perderá 30.")
    print("En caso de perder, perderás 30 puntos de experiencia y el orco ganará 50.")

    opcion = self.elegir_opcion_juego()

    while opcion == 1:
      resultado_ataque = self.simular_ataque(probabilidad_ganar)

      print(f"**{resultado_ataque}!**")

      self.actualizar_estados(resultado_ataque)

      print(f"**Estado actual:**")
      print(self.personaje.get_estado())
      print(self.orco.get_estado())

      probabilidad_ganar = self.calcular_probabilidad_ganar()

      opcion = self.elegir_opcion_juego()

    if opcion == 2:
      print("**Has huido del orco!**")

  def calcular_probabilidad_ganar(self):
    if self.personaje < self.orco:
      probabilidad_ganar = 0.33
    elif self.personaje > self.orco:
      probabilidad_ganar = 0.66
    else:
      probabilidad_ganar = 0.5
    return probabilidad_ganar

  def elegir_opcion_juego(self):
    opcion = int(input("¿Qué deseas hacer? (1) Atacar (2) Huir: "))
    while opcion not in (1, 2):
      opcion = int(input("Opción inválida. Ingrese 1 para atacar o 2 para huir: "))
    return opcion

  def simular_ataque(self, probabilidad_ganar):
    numero_aleatorio = random.uniform(0, 1)
    if numero_aleatorio <= probabilidad_ganar:
      resultado_ataque = "Gana"
    else:
      resultado_ataque = "Pierde"
    return resultado_ataque

  def actualizar_estados(self, resultado_ataque):
    if resultado_ataque == "Gana":
      self.personaje.set_estado(50)
      self.orco.set_estado(-30)
    elif resultado_ataque == "Pierde":
      self.personaje.set_estado(-30)
      self.orco.set_estado(50)

# Crea una instancia del juego
juego = Juego()

# Inicia el juego
juego.iniciar_juego()