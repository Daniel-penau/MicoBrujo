import re
import token

#################################################################################################################################################################################################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#################################################################################################################################################################################################################
#CLASE SCANNER
#Clase que se encarga de escanear los tokens y generar una lista de tokens que contiene objetos Token
class Scanner:
  def __init__(self,linea):
    self.linea = linea.replace('\n', ' \n ') #Separar los \n con espacios
    self.linea = self.linea.split(' ') #Hace lista a base de separar strings por espacios
    self.linea = list(filter(None, self.linea)) #Quitar strings nulos
    self.token_actual = 0
    self.linea_actual = 0
    self.palabra_actual = 0
    self.tokenlst = []
    self.tokenError = []

  def scanCadena(self):
      finalizar = False
      vacio = True
      actual = ""
      if self.token_actual < len(self.linea) and self.linea[self.token_actual][0] == '\"': #Si el token comienza con comillas

         self.tokenlst.append(token.Token("Cadena",str(self.linea[self.token_actual]))) #Concatenar la entidad como parte del token Cadena
         actual = self.linea[self.token_actual]
         pos = 0
         comilla = '\"' #DOBLE COMILLA

         if actual[pos] == comilla: #Si el primer token empieza con comilla
            pos = pos + 1

            while self.token_actual < len(self.linea) and finalizar == False:

                while pos < len(actual) and actual[pos] != comilla: #Recorrer hasta encontrar otro '"'

                      if actual[pos] != ' ': #Si hay algo distinto de espacio
                         vacio = False

                      pos = pos + 1

                if pos >= len(actual): #Si se terminó de recorrer un token sin encontrar comilla
                   self.token_actual = self.token_actual +1

                   if self.token_actual < len(self.linea):
                       self.tokenlst[len(self.tokenlst) -1].appendValor(self.linea[self.token_actual]) #Concatenar la entidad como parte del token Cadena
                       actual = self.linea[self.token_actual]
                       pos = 0

                if self.token_actual < len(self.linea):

                    if actual[pos] == comilla: #Si se encontró comilla

                       if pos == len(actual) -1: #Si la segunda comilla está al final del token respectivo
                           finalizar = True

                       break

         if finalizar == False or vacio == True: #Error si se llego al final de la lista de tokens y no se encontro '"', solo contiene vacio o si la segunda comilla no esta al final del token respectivo
             self.tokenlst.pop() #Eliminar token incompleto
             self.tokenError.append("Error en la palabra numero " + str(self.palabra_actual+1)+", en la linea numero "+ str(self.linea_actual+1))
             self.tokenError.append("Error: se llego al final de la linea y no se encontro '\"', solo contiene vacio entre las comillas o la segunda comilla no finaliza correctamente el token Cadena")
             return "Rechazado" #Token es de tipo Lugar, pero presenta errores de sintaxis

         self.token_actual = self.token_actual +1
         self.palabra_actual = self.palabra_actual+1
         return "Aceptado" #Token es de tipo Lugar y es sintacticamente correcto

      return "Nodeltipo" #Token no empieza con comillas, no es de tipo Lugar




  #Función que escanea a todos los tokens de la gramática
  def scanTokens(self):
    palabras_reservadas = ['mae','mona','diay','upee','sarpe','ni modo','sobrada']
    funciones_predefinidas = ['imprimir()','largo(','indice(','concatenar(','solicitar()','convertir(']


    while self.token_actual < len(self.linea) and self.tokenError == []:

      cadena = self.scanCadena() #Se buscan tokens que sean cadenas de caracteres

      if cadena == "Rechazado":
          continue

      if re.match("[+|-|*|/]",self.linea[self.token_actual]) != None:#Revisa si es token operador
        self.tokenlst.append(token.Token("Operador",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("[0-9]+",self.linea[self.token_actual]) != None: #Revisa si es token numero
        self.tokenlst.append(token.Token("Numero",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual +1
        self.palabra_actual = self.palabra_actual+1

      elif self.linea[self.token_actual] in funciones_predefinidas:
        self.tokenlst.append(token.Token("Funcion",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("^[A-B-a-z-_]+$",self.linea[self.token_actual]) != None and self.linea[self.token_actual]  not in palabras_reservadas :#Revisa si el token es una palabra
        self.tokenlst.append(token.Token("Identificador",str(self.linea[self.token_actual])))                                               #sin comillas que no es una palabra reservada
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("\n",self.linea[self.token_actual]) != None:                        #Revisa si el token es un cambio de linea
        self.tokenlst.append(token.Token("CambioDeLinea",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.linea_actual = self.linea_actual+1
        self.palabra_actual = 0

      elif re.match("sobrada",self.linea[self.token_actual]) != None: #Revisa si el token es un Tipo
        self.tokenlst.append(token.Token("VariableGlobal",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("[()]",self.linea[self.token_actual]) != None:                    #Revisa si el token es un parentesis
        self.tokenlst.append(token.Token("Parentesis",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match(",",self.linea[self.token_actual]) != None:                #Revisa si el token es una Coma
        self.tokenlst.append(token.Token("Coma",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match(";",self.linea[self.token_actual]) != None:                #Revisa si el token es una Coma
        self.tokenlst.append(token.Token("PuntoyComa",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("[{}]",self.linea[self.token_actual]) != None:                    #Revisa si el token es un corchete
        self.tokenlst.append(token.Token("Corchete",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("[&|\|]",self.linea[self.token_actual]) != None:                    #Revisa si el token es un corchete
        self.tokenlst.append(token.Token("OperadorLogico",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match(";",self.linea[self.token_actual]) != None:                #Revisa si el token es una Coma
        self.tokenlst.append(token.Token("PuntoyComa",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1
 
      elif re.match("<|>|<=|>=|==|!=",self.linea[self.token_actual]) != None:        #Revisa si el token es un simbolo comparativo
        self.tokenlst.append(token.Token("Comparativo",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1


      elif re.match("[=]",self.linea[self.token_actual]) != None:                   #Revisa si el token es un simbolo de asignacion
        self.tokenlst.append(token.Token("Asignacion",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("diay",self.linea[self.token_actual]) != None:             #Revisa si el token es un If
        self.tokenlst.append(token.Token("If",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("sarpe",self.linea[self.token_actual]) != None:             #Revisa si el token es un If
        self.tokenlst.append(token.Token("Return",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("ni modo",self.linea[self.token_actual]) != None:             #Revisa si el token es un Else
        self.tokenlst.append(token.Token("Else",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("upee",self.linea[self.token_actual]) != None:                #Revisa si el token es un While
        self.tokenlst.append(token.Token("While",str(self.linea[self.token_actual])))
        self.token_actual = self.token_actual+1
        self.palabra_actual = self.palabra_actual+1

      elif re.match("mae",self.linea[self.token_actual]) != None:
        if  re.match("mona",self.linea[self.token_actual+1]) != None:
               self.tokenlst.append(token.Token("Main",str(self.linea[self.token_actual])+" " +str(self.linea[self.token_actual+1])))
               self.token_actual = self.token_actual+2
               self.palabra_actual = self.palabra_actual+2
        else:
          self.tokenlst.append(token.Token("Funcion",str(self.linea[self.token_actual])))
          self.token_actual = self.token_actual+1
          self.palabra_actual = self.palabra_actual+1
      else:
        #Si el token no es encontrado se agrega el error a la lista de errores
        self.tokenError.append("Error en la palabra numero " + str(self.palabra_actual+1)+", linea numero "+str(self.linea_actual+1)+" : Token "+ str(self.linea[self.token_actual])+" no identificado")
