import transcriptor_2022
import base_palabras
import os
from operator import itemgetter
from tabulate import tabulate
f = transcriptor_2022
bp = base_palabras

def menu_evaluacion_frases():
    print("Entre su opción con el teclado numérico.")
    print("1. Comparar dificultad de dos o más frases.")
    print("2. Ver cualidades de una frase")
    print("3. Acentuación de una palabra")
    opcion_evaluacion_frases = (int(input("Escriba el número 1 o 2 o 3\n")))
    return opcion_evaluacion_frases

def entre_palabra():
    print("Entre la palabra (o pseudopalabra) por la que desea consultar")
    palabra_en_consulta = input("Escriba la palabra:\n")
    palabra_en_consulta = palabra_en_consulta.lower()
    contador_problemas = f.evaluador_normalidad_texto(palabra_en_consulta)
    return palabra_en_consulta

def entre_frases():

    print("Esta aplicación le dirá cuán diferentes son en su dificultad acentual\n una serie de oraciones.\n")
    ene_frases = int(input("¿Cuántas frases desea ingresar?"))

    lista_frases = []
    for i in range(ene_frases):
        frase = input("Ingrese frase: ... ")
        lista_frases.append(frase)

    return lista_frases


def entre_una_frase():

    texto_en_minusculas, texto_sin_puntuacion_split = f.entra_texto()

    contador_problemas = f.evaluador_normalidad_texto(texto_en_minusculas)

    return texto_en_minusculas, texto_sin_puntuacion_split


def analisis_frases_docencia(lista_frases):
    dificultad = []
    for frase in lista_frases:
        texto_en_minusculas = frase.lower()
        texto_sin_puntuacion = texto_en_minusculas.replace(".", "").replace(",", "").replace(";", "").replace("...",
                                                                                                              ""). \
            replace("¡", "").replace("!", "").replace("¿", "").replace("?", "")
        texto_sin_puntuacion_split = texto_sin_puntuacion.split()
        contador_problemas = f.evaluador_normalidad_texto(texto_en_minusculas)

        if contador_problemas == True:
            avance = int(input("Presione cualquier tecla numérica para avanzar"))
            if avance == 1:
                print("Retornar")
                print(input("Presione cualquier tecla"))
                os.system("clear")

        contador_tonicas_monosilabas, contador_atonas_monosilabas, contador_bisilabas_atonas, contador_graves, \
        contador_graves_con_acento_grafico, contador_agudas, contador_agudas_con_acento_grafico, \
        contador_esdrujulas, contador_sobresdrujulas, contador_sec_cerrada_tonica = f.docencia01(
            texto_sin_puntuacion_split)

        total_palabras = (contador_atonas_monosilabas + contador_tonicas_monosilabas + contador_bisilabas_atonas \
                          + contador_graves + contador_agudas + contador_esdrujulas + contador_sobresdrujulas)

        diversidad_de_palabras = 0
        contador_dificultad = 0

        if contador_esdrujulas >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_esdrujulas * 2)

        if contador_atonas_monosilabas >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_atonas_monosilabas * 1)

        if contador_tonicas_monosilabas >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_tonicas_monosilabas * 2)

        if contador_bisilabas_atonas >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_bisilabas_atonas * 1)

        if contador_agudas >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_agudas * 2)

        if contador_graves_con_acento_grafico >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_graves * 2)

        if (contador_graves - contador_graves_con_acento_grafico) >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_graves * 1)

        if contador_sec_cerrada_tonica >= 1:
            diversidad_de_palabras = diversidad_de_palabras + 1
            contador_dificultad = contador_dificultad + (contador_sec_cerrada_tonica * 2)

        grado_de_dificultad_acentual = f.indice_dificultad_acentual(total_palabras, \
                                                                    diversidad_de_palabras, \
                                                                    contador_dificultad)

        dificultad.append(grado_de_dificultad_acentual)

    agrupar_frase_dificultad = zip(lista_frases, dificultad)

    lista_agrupada_frase_dificultad =list(agrupar_frase_dificultad)

    ordenada = sorted(lista_agrupada_frase_dificultad, key= itemgetter(1))

    print(tabulate(ordenada, headers = ['frase', 'Dificultad']))


def cualidades_una_frase(texto_sin_puntuacion_split):

        lista_palabras = f.analisis_compuestas(texto_sin_puntuacion_split)

        contador_tonicas_monosilabas, contador_atonas_monosilabas, contador_bisilabas_atonas, contador_graves, \
        contador_graves_con_acento_grafico, contador_agudas, contador_agudas_con_acento_grafico, \
        contador_esdrujulas, contador_sobresdrujulas, contador_sec_cerrada_tonica = f.docencia01(texto_sin_puntuacion_split)


        print(texto_sin_puntuacion_split)
        print("==========")

        propiedades = [["Monosílabos átonos", contador_atonas_monosilabas], ["Monosílabos tónicos", contador_tonicas_monosilabas],
                       ["Bisílabos átonos", contador_bisilabas_atonas],
                       ["Agudas con tilde", contador_agudas_con_acento_grafico],
                       ["Agudas sin tilde",(contador_agudas-contador_agudas_con_acento_grafico)],
                       ["Graves con tilde", contador_graves_con_acento_grafico],
                       ["Graves sin tilde", (contador_graves-contador_graves_con_acento_grafico)],
                       ["Esdrújulas", contador_esdrujulas],
                       ["Sobresdrújulas", contador_sobresdrujulas],
                       ["TOTAL:", len(texto_sin_puntuacion_split)]]
        print(tabulate(propiedades, headers = ["Tipo de palabra", "Ocurrencias"]))


opcion_evaluacion_frases = menu_evaluacion_frases()

if opcion_evaluacion_frases == 1:
    lista_frases = entre_frases()
    analisis_frases_docencia(lista_frases)
elif opcion_evaluacion_frases == 2:
    texto_en_minusculas, texto_sin_puntuacion_split = entre_una_frase()
    cualidades_una_frase(texto_sin_puntuacion_split)
elif opcion_evaluacion_frases == 3:
    palabra_en_consulta = entre_palabra()
    lista_palabra = []
    lista_palabra.append(palabra_en_consulta)

    contador_tonicas_monosilabas, contador_atonas_monosilabas, contador_bisilabas_atonas, contador_graves, \
    contador_graves_con_acento_grafico, contador_agudas, contador_agudas_con_acento_grafico, \
    contador_esdrujulas, contador_sobresdrujulas, contador_sec_cerrada_tonica = f.docencia01(lista_palabra)

    if contador_sobresdrujulas > 0:
        print("La palabra es sobresdrújula")
    elif contador_esdrujulas > 0:
        print("La palabra es esdrújula")
    elif contador_graves > 0:
        print("La palabra es grave.")
        for secuencia in bp.secuencia_cerrada_tonica_mas_abierta:
            if secuencia in palabra_en_consulta:
                print("Se escribe con acento porque contiene una secuencia con cerrada tónica + abierta")
                quit()

        if (palabra_en_consulta[-1]=="a" or palabra_en_consulta[-1] == "e" or palabra_en_consulta[-1] == "i" or \
            palabra_en_consulta[-1] == "o" or palabra_en_consulta[-1]== "u" or palabra_en_consulta[-1] == "n" or \
            palabra_en_consulta[-1] == "s") and ("á" in palabra_en_consulta or "é" in palabra_en_consulta \
                                                 or "í" in palabra_en_consulta or "ó" in palabra_en_consulta \
                                                 or "ú" in palabra_en_consulta):
            print("La palabra es grave y se debe escribir sin acento")

    elif contador_agudas > 0:
        print("La palabra es aguda")
        largo_palabra_en_consulta = len(palabra_en_consulta)
        pre_palabra_en_consulta = palabra_en_consulta[0:-1]
        if palabra_en_consulta[-1] != "á" or palabra_en_consulta[-1] != "é" or palabra_en_consulta[-1] != "í" or \
                palabra_en_consulta[-1] != "ó" or palabra_en_consulta[-1] != "ú":
            if "á" in pre_palabra_en_consulta or "é" in pre_palabra_en_consulta or "í" in pre_palabra_en_consulta or\
                    "ó" in pre_palabra_en_consulta or "ú" in pre_palabra_en_consulta:
                print("Se debe escribir sin acento")
