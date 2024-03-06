class Personaje:

  def __init__(self, nombre):
    self.nombre = nombre
    self.nivel = 1
    self.experiencia = 0

  def get_estado(self):
    return f"{self.nombre} (Nivel: {self.nivel}, Experiencia: {self.experiencia})"

  def set_estado(self, experiencia):
    experiencia_total = self.experiencia + experiencia
    while experiencia_total >= 100:
      self.nivel += 1
      experiencia_total -= 100
    self.experiencia = experiencia_total

  def __gt__(self, otro_personaje):
    return self.nivel > otro_personaje.nivel

  def __lt__(self, otro_personaje):
    return self.nivel < otro_personaje.nivel