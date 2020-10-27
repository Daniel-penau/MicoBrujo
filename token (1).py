#################################################################################################################################################################################################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#################################################################################################################################################################################################################
#CLASE TOKEN
#Clase que guarda el tipo y el valor/contenido de un token
class Token:
  tipo = ""
  valor = ""

  def __init__(self,tipo,valor): #Constructor
    self.tipo = tipo
    self.valor = valor

  def getTipo(self): #Función que obtiene el tipo del token
    return self.tipo

  def getValor(self): #Función que obtiene el valor del token
    return self.valor

  def appendValor(self,valor): #Función que concatena una hilera a la hilera valor
    self.valor = self.valor +" "+ valor

  def printToken(self): #Función que imprime el token con el formato de salida
    print("<"+self.tipo+","+self.valor+">")
