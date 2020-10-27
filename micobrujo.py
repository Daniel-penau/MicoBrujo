import os
import scanner

def main():
    #filename = input("Escriba el nombre del archivo (sin extension): ")
    filename = "Pruebas.txt"

    if not os.path.exists(filename):
        print("El archivo no existe")
        return 0

    f = open(filename, "r")

    line = f.read() #Extrae un string que contiene todos los caracteres del archivo

    print("")
    print("")
    print("SALIDA DEL COMPILADOR")

    print("")

    resultadoScanner = scanner.Scanner(line)
    resultadoScanner.scanTokens()
    token = 0
    error = False

    if resultadoScanner.tokenError != []:
        error = True
        for error in resultadoScanner.tokenError:
            print(error)

    if not error:

        #Imprimir tokens
        while token < len(resultadoScanner.tokenlst) and error == False:
            resultadoScanner.tokenlst[token].printToken()
            token+=1



if __name__== "__main__":
    main()
