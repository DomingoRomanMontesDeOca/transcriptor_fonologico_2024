import operator
import os
import re
import readline
import matplotlib.pyplot as plt
import base_palabras

bp = base_palabras


def menu_general():
    os.system("clear")
    print("Opciones generales del programa")
    print("===============================")
    print("Use teclado numérico para responder")
    print("")
    print("Opciones:")
    print("")
    print("\t1. Cuestiones relativas a los fonemas")
    print("")
    print("\t2. Cuestiones relativas a las sílabas")
    print("")
    print("\t3. Cuestiones relativas a las palabras")
    print("")
    print("\t9. Salir")

    print("===============================")
    opcion_general = int(input("Use teclado numérico para indicar su opción:   "))
    print("")
    print("===============================")
    os.system("clear")
    return opcion_general


def volver_a_ejecutar():
    volver = int(input(" 1: volver al menú principal:\n 0: salir\n"))
    if volver == 1:
        opcion_general = True
    else:
        exit()


def menu_fonemas():
    print("==============================")
    print("\t1. Transcripción fonológica")
    print("")
    print("\t2. Recuento total de fonemas")
    print("")
    print("\t3. Gráficos de ocurrencias de fonemas")
    print("==============================")
    opcion_fonemas = int(input("Use teclado numérico para indicar su opción:   "))
    os.system("clear")
    return opcion_fonemas


def menu_silabas():
    print("==============================")
    print("\t1. Transcripción silábica")
    print("")
    print("\t2. Recuento de tipos silábicos")
    print("")
    print("\t3. Gráficos de ocurrencias de tipos silábicos")
    print("==============================")

    opcion_silabas = int(input("Use teclado numérico para indicar su opción:   "))
    os.system("clear")
    return opcion_silabas


def menu_palabras():
    print("==============================")
    print("\t1. Recuento de palabras tónicas y átonas")
    print("")
    print("\t2. Recuento de tipos de palabras tónicas y átonas")
    print("")
    print("\t3. Recuento de letras finales en los principales tipos acentuales de palabras")
    print("")
    print("\t4. Gráficos de tipos de palabras")
    print("")
    print("\t5. Utilidades docentes")
    print("==============================")
    opcion_palabras = int(input("Use teclado numérico para indicar su opción:   "))
    os.system("clear")
    return opcion_palabras


def entra_texto():
    """
    Recibe como entrada un texto
    y retorna la conversión a minúsculas del mismo.

    Retorna también texto minúscula sin puntuación.
    """
    texto = input("Texto:   ")
    # sustituye abreviaturas comunes
    texto = texto.replace("Ud.", "usted").replace("Uds.", "Ustedes").replace("etc.", "etcétera").replace("Dr.",
                                                                                                         "doctor") \
        .replace("Dra.", "doctora").replace("Atte.", "atentamente").replace("FFAA", "fuerzas armadas") \
        .replace("FF.AA", "fuerzas armadas").replace("Ltda.", "limitada").replace("Stgo.", "santiago")

    texto_en_minusculas = texto.lower()

    texto_sin_puntuacion = texto_en_minusculas.replace(".", "").replace(",", "").replace(";", "").replace("...", ""). \
        replace("¡", "").replace("!", "").replace("¿", "").replace("?", "")

    texto_sin_puntuacion_split = texto_sin_puntuacion.split()

    contador_problemas = evaluador_normalidad_texto(texto_en_minusculas)

    if contador_problemas == True:
        avance = int(input("Presione cualquier tecla numérica para avanzar"))
        if avance == 1:
            print("Retornar")
            print(input("Presione cualquier tecla"))
            os.system("clear")

    return texto_en_minusculas, texto_sin_puntuacion_split


def evaluador_normalidad_texto(texto_en_minusculas):
    """ Busca:
                caracteres numéricos
                secuencias anómalas de letras
                caracteres especiales
        Avisa e imprime en pantalla la primera secuencia anómala
     """
    # buscar  comillas curvas
    # buscar todos los tipos de guiones

    anomalia_letras = re.search("bb|ccc,|ddd|ff|gg|hh|jj|kk|lll|mm|nnn|ññ|pp|qq|rrr|sss|tt|vv|xx|yy|zz|chch|ququ|aaa\
    |eee|ii|ooo|uu|bx|by|bw|cg|cf|cj|ck|cm|cñ|cp|cw|cx|cy|cz|df|dg|dk|dñ|dp|dw|dx|dz\
    |fb|fc|fd|fg|fh|fj|fk|fm|fn|fñ|fp|fq|fs|ft|fv|fw|fx|fy|fz\
    |gb|gc|gf|gh|gj|gk|gñ|gp|gq|gs|gt|gv|gw|gx|gy|gz\
    |hb|hc|hd|hf|hg|hj|hk|hl|hm|hn|hñ|hp|hq|hr|hs|ht|hv|hw|hx|hy|hz\
    |jb|jc|jd|jf|jg|jh|jk|jl|jm|jn|jñ|jp|jq|jr|js|jt|jv|jw|jx|jy|jz\
    |kb|kc|kd|kf|kg|kh|kj|kl|km|kn|kñ|kp|kq|kr|ks|kt|kv|kw|kx|ky|kz\
    |lw|lx|ly\
    |mñ|mv|mx|my|mz\
    |nb|ny|nw\
    |ñb|ñc|ñd|ñf|ñg|ñh|ñj|ñk|ñl|ñp|ñq|ñr|ñs|ñt|ñv|ñw\
    |pb|pd|pf|pg|ph|pj|pk|pm|pñ|pq|pv|pw|px|py|pz\
    |qa|qe|qi|qo|qb|qc|qd|qf|qh|qj|qk|ql|qm|qn|qñ|qp|qr|qs|qt|qv|qw|qx|qy|qz\
    |rx|rw|ry\
    |sw|sy\
    |tx|tw\
    |vx|vw\
    |xw|xy\
    |yb|yc|yd|yf|yg|yh|yj|yk|yl|ym|yn|yñ|yp|yq|yr|ys|yt|yv|yw|yz\
    |zd|zf|zh|zj|zk|zñ|zw|zy\
    |frb|frc|frd|frf|frg|frv|bnr", texto_en_minusculas)

    anomalia_numero = re.search("\d", texto_en_minusculas)

    # problemas con algunos caracteres

    anomalia_caracteres_especiales = re.search("=|#|¢|%|@|&|[$]|ª|º|-|_", texto_en_minusculas)

    contador_problemas = 0

    if anomalia_numero:
        caso_numero = anomalia_numero.group()
        contador_problemas = contador_problemas + 1
        print("Anómalo. El texto contiene a lo menos un número")
        print(caso_numero)
    if anomalia_letras:
        caso_letra = anomalia_letras.group()
        contador_problemas = contador_problemas + 1
        print("Anómalo. El texto contiene secuencias sospechosas")
        print(caso_letra)
    if anomalia_caracteres_especiales:
        caso_caracter = anomalia_caracteres_especiales.group()
        contador_problemas = contador_problemas + 1
        print("Anómalo. El texto contiene caracteres especiales")
        print(caso_caracter)
    if contador_problemas > 1:
        print("Persisten dramas")
        input("Presione una tecla")
        os.system("clear")
    elif contador_problemas == 0:
        print("Avance al análisis")
        input("Presione una tecla")
        os.system("clear")

    return contador_problemas


def docencia01(texto_sin_puntuacion_split):

    lista_palabras = analisis_compuestas(texto_sin_puntuacion_split)
    lista_compleja_palabras = identificador_silaba_tonica(lista_palabras)

    total_palabras, contador_atonas, contador_tonicas, contador_bisilabas_atonas, contador_atonas_monosilabas, \
    contador_tonicas_monosilabas, contador_agudas, contador_graves, contador_esdrujulas, contador_sobresdrujulas \
        = contador_palabras(lista_compleja_palabras)

    contador_graves_con_acento_grafico = 0
    contador_agudas_con_acento_grafico = 0
    contador_sec_cerrada_tonica = 0

    for item in lista_compleja_palabras:
        if item[-3] == '-2':
            for fonema in item[0]:
                if fonema in bp.vocales_acentuadas:
                    contador_graves_con_acento_grafico = contador_graves_con_acento_grafico + 1
        elif item[-3] == '-1':
            for fonema in item[0]:
                if fonema in bp.vocales_acentuadas:
                    contador_agudas_con_acento_grafico = contador_agudas_con_acento_grafico + 1


    for item in lista_compleja_palabras:
        for dip in bp.secuencia_cerrada_tonica_mas_abierta:
            if dip in item[0]:
                contador_sec_cerrada_tonica = contador_sec_cerrada_tonica + 1

    return contador_tonicas_monosilabas, contador_atonas_monosilabas, contador_bisilabas_atonas, contador_graves, \
           contador_graves_con_acento_grafico, contador_agudas, contador_agudas_con_acento_grafico,\
           contador_esdrujulas, contador_sobresdrujulas, contador_sec_cerrada_tonica


def indice_dificultad_acentual(longitud, diversidad_palabras, dificultad):

    if longitud >= 15:
        diversidad_posible = 10
    elif longitud > 10 and longitud < 15:
        diversidad_posible = 9
    elif longitud >= 6  and longitud <= 10:
        diversidad_posible = 8
    elif longitud <= 5:
        diversidad_posible = 6

    referencia_dificultad = longitud * (longitud * 2)

    dificultad_frase = longitud * dificultad


#   (número de palabras * 2 (máxima dificultad) * dificultad real
    grado_de_dificultad_acentual = referencia_dificultad /  dificultad_frase

    return grado_de_dificultad_acentual


def analisis_compuestas(texto_sin_puntuacion_split):
    """
    lista palabras es la lista de palabras del texto
    pero con separación en dos palabras de aquellas que son
    palabras compuestas, como ético-crítico, sutilmente.
    Todas las palabras terminadas en -mente
    serán descompuestas; sin embargo esto no afecta el resultado final
    """
    lista_palabras = []

    for palabra in texto_sin_puntuacion_split:

        hasta_guion = palabra.find("-")

        if palabra.endswith("mente") and len(palabra) > 5:
            item_1 = palabra[0:-5]
            item_2 = "mente"
            lista_palabras.append(item_1)
            lista_palabras.append(item_2)

        elif hasta_guion != -1:
            punto_del_guion = hasta_guion
            largo_palabra = len(palabra)
            item_1 = palabra[0:punto_del_guion]
            item_2 = palabra[punto_del_guion + 1:largo_palabra]
            lista_palabras.append(item_1)
            lista_palabras.append(item_2)
        else:
            lista_palabras.append(palabra)

    return lista_palabras


def identificador_silaba_tonica(lista_palabras):
    # La lista compleja de palabras tiene [palabra, palabra sin consonantes, tónica o átona y posición sílaba tónica]

    lista_compleja_palabras = []

    for palabra in lista_palabras:

        palabra_sin_diptongos = cambia_a_sin_diptongos(palabra)

        texto_sin_grafemas_consonantes, ultimo_caracter = elimina_grafemas_consonantes(palabra_sin_diptongos)

        ene_silabas = len(texto_sin_grafemas_consonantes)

        if ene_silabas == 1:
            if palabra in bp.monosilabos_atonos:
                pal_tonica = False
                posicion_tonica = "0"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])

            elif palabra not in bp.monosilabos_atonos:
                pal_tonica = True
                posicion_tonica = "1"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])

        elif ene_silabas == 2 and palabra in bp.bisilabos_atonos:
            pal_tonica = False
            posicion_tonica = "0"
            lista_compleja_palabras.append(
                [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])

        elif ene_silabas >= 2:

            pal_tonica = True

            if ene_silabas > 3 and texto_sin_grafemas_consonantes[-4] in bp.vocales_acentuadas:
                posicion_tonica = "-4"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])
            elif ene_silabas > 2 and texto_sin_grafemas_consonantes[-3] in bp.vocales_acentuadas:
                posicion_tonica = "-3"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])
            # graves y agudas con acento escrito

            elif ene_silabas > 1 and texto_sin_grafemas_consonantes[-2] in bp.vocales_acentuadas:
                posicion_tonica = "-2"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])

            elif ene_silabas > 1 and texto_sin_grafemas_consonantes[-1] in bp.vocales_acentuadas:
                posicion_tonica = "-1"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])

            # graves y agudas sin acento escrito
            elif ene_silabas > 1 and ((texto_sin_grafemas_consonantes[-2] not in bp.vocales_acentuadas) and (
                    texto_sin_grafemas_consonantes[-1] not in bp.vocales_acentuadas)) and \
                    (ultimo_caracter not in bp.revision_grafema_final):
                posicion_tonica = "-1"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])

            elif ene_silabas > 1 and ((texto_sin_grafemas_consonantes[-1] not in bp.vocales_acentuadas) and (
                    texto_sin_grafemas_consonantes[-2] not in bp.vocales_acentuadas)) and \
                    ultimo_caracter in bp.revision_grafema_final:
                posicion_tonica = "-2"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter, ene_silabas])

    return lista_compleja_palabras


def contador_palabras(lista_compleja_palabras):
    total_palabras = len(lista_compleja_palabras)

    contador_tonicas = 0
    contador_atonas = 0

    contador_atonas_monosilabas = 0
    contador_tonicas_monosilabas = 0
    contador_bisilabas_atonas = 0

    contador_sobresdrujulas = 0
    contador_esdrujulas = 0
    contador_graves = 0
    contador_agudas = 0

    for palabra in lista_compleja_palabras:
        if True == palabra[2]:
            contador_tonicas = contador_tonicas + 1
            if palabra[5] == 1:
                contador_tonicas_monosilabas = contador_tonicas_monosilabas + 1
            elif palabra[5] > 1:
                if palabra[3] == "-4":
                    contador_sobresdrujulas = contador_sobresdrujulas + 1
                elif palabra[3] == "-3":
                    contador_esdrujulas = contador_esdrujulas + 1
                elif palabra[3] == "-2":
                    contador_graves = contador_graves + 1
                elif palabra[3] == "-1":
                    contador_agudas = contador_agudas + 1

        elif False == palabra[2]:
            contador_atonas = contador_atonas + 1
            if palabra[5] == 1:
                contador_atonas_monosilabas = contador_atonas_monosilabas + 1
            elif palabra[5] == 2:
                contador_bisilabas_atonas = contador_bisilabas_atonas + 1

    return total_palabras, contador_atonas, contador_tonicas, contador_bisilabas_atonas, contador_atonas_monosilabas, \
           contador_tonicas_monosilabas, contador_agudas, contador_graves, contador_esdrujulas, contador_sobresdrujulas


def transcriptor(texto_en_minusculas):
    """
    Recibe como entrada texto_en_minusculas
        hace la transcripción fonológica en varios pasos
        vocales acentuadas gráficamente se representan en mayúsculas.
    Esta información será útil para la tonicidad de las palabras.
    """

    # Primeras sustituciones
    ##  finales diptongos conserva las tónicas en mayúsculas
    ##  consonantes

    # En estos remplazos, las vocales tildadas se transcriben con mayúscula
    remplazos = [("oy ", "oi "), ("oy,", "oi,"), ("oy.", "oi."), ("oy;", "oi;"),
                 ("oy)", "oi)"), ("oy?", "oi?"), ("oy!", "oi!"),
                 ("ey ", "ei "), ("ey,", "ei,"), ("ey.", "ei."), ("ey;", "ei;"),
                 ("ey)", "ei)"), ("ey?", "ei?"), ("ey!", "ei!"),
                 ("uy ", "ui "), ("uy,", "ui,"), ("uy.", "ui."), ("uy;", "ui;"),
                 ("uy)", "ui)"), ("uy?", "ui?"), ("uy!", "ui!"),
                 ("ay ", "ai "), ("ay,", "ai,"), ("ay.", "ai."), ("ay;", "ai;"),
                 ("ay)", "ai)"), ("ay?", "ai?"), ("ay!", "ai!"),
                 ("óy ", "Oi "), ("óy,", "Oi,"), ("óy.", "Oi."), ("óy;", "Oi;"),
                 ("óy)", "Oi)"), ("óy?", "Oi?"), ("óy!", "Oi!"),
                 ("éy ", "Ei "), ("éy,", "Ei,"), ("éy.", "Ei."), ("éy;", "Ei;"),
                 ("éy)", "Ei)"), ("éy?", "Ei?"), ("éy!", "Ei!"),
                 ("úy ", "Ui "), ("úy,", "Ui,"), ("úy.", "Ui."), ("úy;", "Ui;"),
                 ("úy)", "Ui)"), ("úy?", "Ui?"), ("úy!", "Ui!"),
                 ("áy ", "Ai "), ("áy,", "Ai,"), ("áy.", "Ai."), ("áy;", "Ai;"),
                 ("áy)", "Ai)"), ("áy?", "Ai?"), ("áy!", "Ai!"),
                 ## consonantes
                 ("v", "b"),
                 ("ce", "se"), ("ci", "si"), ("cé", "sE"), ("cí", "sI"),
                 ("ca", "ka"), ("co", "ko"), ("cu", "ku"),
                 ("cá", "kA"), ("có", "kO"), ("cú", "kU"),
                 ("cr", "kɾ"),
                 ("ch", "∫"),
                 ("c", "k"),
                 (" x", "s"), ("x", "ks"), ("meksi", "mexi"),
                 ("j", "x"), ("ge", "xe"), ("gi", "xi"),
                 ("w", "g"),
                 ("ya", "ça"), ("ye", "çe"), ("yi", "çi"), ("yo", "ço"), ("yu", "çu"),
                 ("yá", "çA"), ("yé", "çE"), ("yí", "çI"), ("yó", "çO"), ("yú", "çU"),
                 ("ny", "nç"),
                 ("y", "i"), ("ll", "ç"), ("qu", "k"),
                 ("z", "s"), ("gue", "ge"), ("gui", "gi"), ("rr", "00"), ("ar", "aɾ"), ("er", "eɾ"), ("ir", "iɾ"),
                 ("or", "oɾ"), ("ur", "uɾ"),
                 ("gué", "gE"), ("guí", "gI"), ("ár", "Aɾ"), ("ér", "Eɾ"), ("ír", "Iɾ"),
                 ("ór", "Oɾ"), ("úr", "Uɾ"),
                 ("gr", "gɾ"), ("br", "bɾ"), ("pr", "pɾ"), ("tr", "tɾ"), ("dr", "dɾ"),
                 ("fr", "fɾ"), ("cl", "kl"), ("00", "r"), ("h", ""), ("ü", "u")]

    transcripcion_1 = texto_en_minusculas

    for remplazoFonemas in remplazos:
        transcripcion_1 = transcripcion_1.replace(remplazoFonemas[0], remplazoFonemas[1])

    remplazos_2 = [("á", "A"), ("é", "E"), ("í", "I"), ("ó", "O"), ("ú", "U")]

    for remplazo2 in remplazos_2:
        transcripcion_1 = transcripcion_1.replace(remplazo2[0], remplazo2[1])

    pausas = [(",", "|"), (".", "‖ "), (";", "‖ "), (":", "| "), ("…", "| "), ("...", "| "), ("-", "| "),
              ("¿", ""), ("?", "‖ "), ("¡", ""), ("!", "‖ "), ("(", "| "), (")", "|"), ('"', '|'), ("'", "|")]

    transcripcion_2 = transcripcion_1

    for sust_pausa in pausas:
        transcripcion_2 = transcripcion_2.replace(sust_pausa[0], sust_pausa[1])

    # b transcripción 2 con ∫ para che, ç = ye; ñ.

    #    transcripcion_3 = transcripcion_2.replace ( '∫', 't͡∫' ).replace ( "I", "i" ).replace ( "U", "u" ).\
    #       replace ( "A", "a" ).replace ( "E", "e" ).replace ( "O", "o" ).replace ( "ç", "ʝ" ).replace ( "ñ", "ɲ" )

    # Instala los archifonemas
    transcripcion_4 = transcripcion_2.replace('n b', 'N b').replace('m b', 'N b').replace('m n', 'N n'). \
        replace('n d', 'N d').replace('n f', 'N f').replace('n g', 'N g').replace('n x', 'N x'). \
        replace('n k', 'N k').replace('n l', 'N l').replace('n m', 'N m').replace('n n', 'N n'). \
        replace('n ñ', 'N ñ').replace('n p', 'N p').replace('n r', 'N r').replace('n s', 'N s'). \
        replace('n t', 'N t').replace('n ç', 'N ç').replace('nb', 'Nb').replace('mb', 'Nb'). \
        replace('mn', 'Nm'). \
        replace('n∫', 'N∫').replace('nd', 'Nd').replace('nf', 'Nf').replace('ng', 'Ng'). \
        replace('nx', 'Nx').replace('nk', 'Nk').replace('nl', 'Nl').replace('nm', 'Nm'). \
        replace('nn', 'Nn').replace('np', 'Np').replace('nr', 'Nr').replace('ns', 'Ns'). \
        replace('nt', 'Nt').replace('n|', 'N|').replace('n‖', 'N‖').replace('m|', 'N|'). \
        replace('mp', 'Np').replace('mb', 'Nb').replace('m p', 'N p').replace('m b', 'N b'). \
        replace('m‖', 'N‖').replace('ɾ b', 'R b').replace('ɾ ∫', 'R ∫').replace('ɾ d', 'R d'). \
        replace('ɾ f', 'R f').replace('ɾ g', 'R g').replace('ɾ x', 'R x').replace('ɾ k', 'R k'). \
        replace('ɾ l', 'R l').replace('ɾ m', 'R m').replace('ɾ R', 'ɾ R').replace('ɾ ɲ', 'R ɲ'). \
        replace('ɾ p', 'R p').replace('ɾ r', 'R r').replace('ɾ s', 'R s').replace('ɾ t', 'R t'). \
        replace('ɾ y', 'R y').replace('ɾb', 'Rb').replace('ɾ∫', 'R∫').replace('ɾd', 'Rd'). \
        replace('ɾf', 'Rf').replace('ɾg', 'Rg').replace('ɾx', 'Rx').replace('ɾk', 'Rk'). \
        replace('ɾl', 'Rl').replace('ɾm', 'Rm').replace('ɾR', 'ɾR').replace('ɾñ', 'Rñ'). \
        replace('ɾp', 'Rp').replace('ɾr', 'Rr').replace('ɾs', 'Rs').replace('ɾt', 'Rt'). \
        replace('ɾç', 'Rç').replace('ɾ|', 'R|').replace('ɾ‖', 'R‖').replace('b b', 'B b'). \
        replace('b d', 'B d'). \
        replace('b f', 'B f').replace('b g', 'B g').replace('b x', 'B x').replace('b k', 'B k'). \
        replace('b l', 'B l').replace('b m', 'B m').replace('b r', 'B r').replace('b ɲ', 'B ñ'). \
        replace('b p', 'B p').replace('b s', 'B s').replace('b t', 'B t').replace('b y', 'B y'). \
        replace('bb', 'Bb').replace('b∫', 'B∫').replace('bd', 'Bd').replace('bf', 'Bf'). \
        replace('bg', 'Bg').replace('bx', 'Bx').replace('bk', 'Bk').replace('bm', 'Bm'). \
        replace('bñ', 'Bñ').replace('bp', 'Bp').replace('bs', 'Bs').replace('bt', 'Bt'). \
        replace('bʝ', 'Bʝ').replace('p b', 'p b').replace('p ∫', 'p ∫').replace('p d', 'p d'). \
        replace('p f', 'p f').replace('p g', 'p g').replace('p x', 'p x').replace('p k', 'p k'). \
        replace('p l', 'p l').replace('p m', 'p m').replace('p r', 'p r').replace('p ñ', 'p ñ'). \
        replace('p p', 'p p').replace('p s', 'p s').replace('p t', 'p t').replace('p ç', 'p ç'). \
        replace('pb', 'Bb').replace('p∫', 'B∫').replace('pd', 'Bd').replace('pf', 'Bf'). \
        replace('pg', 'Bg').replace('px', 'Bx').replace('pk', 'Bk').replace('pm', 'Bm'). \
        replace('pñ', 'Bñ').replace('pp', 'Bp').replace('ps', 'Bs').replace('pt', 'Bt'). \
        replace('pç', 'Bç').replace('p‖', 'B‖').replace('b|', 'B|').replace('b‖', 'B‖'). \
        replace('d b', 'D b').replace('d ∫', 'D ∫').replace('d d', 'D d').replace('d f', 'D f'). \
        replace('d g', 'D g').replace('d x', 'D x').replace('d k', 'D k').replace('d l', 'D l'). \
        replace('d m', 'D m').replace('d r', 'D r').replace('d ñ', 'D ñ'). \
        replace('d p', 'D p').replace('d r', 'D r').replace('d s', 'D s').replace('d t', 'D t'). \
        replace('d ç', 'D ç').replace('db', 'Db').replace('d∫', 'D∫').replace('df', 'Df'). \
        replace('dg', 'Dg').replace('dx', 'Dx').replace('dk', 'Dk'). \
        replace('dl', 'Dl').replace('dm', 'Dm').replace('dñ', 'Dñ').replace('dp', 'Dp'). \
        replace('ds', 'Ds').replace('dt', 'Dt').replace('dç', 'Dç').replace('d|', 'D|'). \
        replace('d‖', 'D‖').replace('t b', 'D b').replace('t c', 'D c').replace('t d', 'D d'). \
        replace('t f', 'D f').replace('t g', 'D g').replace('t x', 'D x').replace('t k', 'D k'). \
        replace('t l', 'D l').replace('t m', 'D m').replace('t r', 'D r').replace('t ñ', 'D ñ'). \
        replace('t p', 'D p').replace('t r', 'D r').replace('t s', 'D s').replace('t t', 'D t'). \
        replace('t ç', 'D ç').replace('tb', 'Db').replace('t∫', 'D∫').replace('td', 'Dd'). \
        replace('tf', 'Df').replace('tg', 'Dg').replace('tx', 'Dx').replace('tk', 'Dk'). \
        replace('tm', 'Dm').replace('tñ', 'Dñ').replace('tp', 'Dp').replace('ts', 'Ds'). \
        replace('tt', 'Dt').replace('tç', 'Dç').replace('t|', 'D|').replace('t‖', 'D‖'). \
        replace('g b', 'G b').replace('g d', 'G d').replace('g ∫', 'G ∫').replace('g d', 'G d'). \
        replace('g f', 'G f').replace('g g', 'G g').replace('g x', 'G x'). \
        replace('g k', 'G k').replace('g l', 'G l').replace('g m', 'G m').replace('g r', 'G r'). \
        replace('g ñ', 'G ñ').replace('g p', 'G p').replace('g r', 'G r').replace('g s', 'G s'). \
        replace('g t', 'G t').replace('g ç', 'G ç').replace('gb', 'Gb').replace('gd', 'Gd'). \
        replace('g∫', 'G∫').replace('gd', 'Gd').replace('gf', 'Gf').replace('gg', 'Gg'). \
        replace('gx', 'Gx').replace('gk', 'Gk').replace('gm', 'Gm').replace('gñ', 'Gñ'). \
        replace('gp', 'Gp').replace('gs', 'Gs').replace('gt', 'Gt').replace('gç', 'Gç'). \
        replace('g|', 'G|').replace('g‖', 'G‖').replace('k b', 'G b').replace('k d', 'G d'). \
        replace('k ∫', 'G ∫').replace('k d', 'G d').replace('k f', 'G f').replace('k g', 'G g'). \
        replace('k x', 'G x').replace('k k', 'G k').replace('k l', 'G l').replace('k m', 'G m'). \
        replace('k r', 'G r').replace('k ñ', 'G ñ').replace('k p', 'G p').replace('k r', 'G r'). \
        replace('k s', 'G s').replace('k t', 'G t').replace('k ç', 'G ç').replace('kb', 'Gb'). \
        replace('kd', 'Gd').replace('k∫', 'G∫').replace('kd', 'Gd').replace('kf', 'Gf'). \
        replace('kg', 'Gg').replace('kx', 'Gx').replace('kk', 'Gk').replace('km', 'Gm'). \
        replace('kñ', 'Gñ').replace('kp', 'Gp').replace('ks', 'Gs').replace('kt', 'Gt'). \
        replace('kç', 'Gç').replace('k|', 'G|').replace('k‖', 'G‖')

    transcripcion_5 = transcripcion_4.replace('∫', 't͡∫').replace("I", "i").replace("U", "u"). \
        replace("A", "a").replace("E", "e").replace("O", "o").replace("ç", "ʝ").replace("ñ", "ɲ")

    return transcripcion_1, transcripcion_2, transcripcion_4, transcripcion_5


def cambia_a_sin_diptongos(texto):
    texto_sin_diptongos = texto. \
        replace("au", "a").replace("ai", "a").replace("ia", "a").replace("ua", "a"). \
        replace("áu", "á").replace("ái", "á").replace("iá", "á").replace("uá", "á"). \
        replace("ui", "i").replace("iu", "u"). \
        replace("eu", "e").replace("ue", "e").replace("ei", "e").replace("ie", "e"). \
        replace(" éu", "é").replace("ué", "é").replace("éi", "é").replace("ié", "é"). \
        replace("ou", "o").replace("uo", "o").replace("io", "o").replace("oi", "o"). \
        replace("óu", "ó").replace("uó", "ó").replace("ió", "ó").replace("ói", "ó")
    return (texto_sin_diptongos)


def elimina_grafemas_consonantes(texto_sin_diptongo):
    texto = texto_sin_diptongo
    ultimo_caracter = texto[-1]

    texto_sin_grafemas_consonantes = texto.replace("b", "").replace("c", "").replace("d", ""). \
        replace("f", "").replace("gue", "e").replace("gui", "i"). \
        replace("gü", "u").replace("g", "").replace("h", "").replace("j", ""). \
        replace("k", "").replace("l", "").replace("m", "").replace("n", ""). \
        replace("ñ", "").replace("p", "").replace("q", "").replace("r", ""). \
        replace("s", "").replace("t", "").replace("v", "").replace("x", ""). \
        replace(" y ", "  ").replace("y, ", " ").replace("z", "")

    return texto_sin_grafemas_consonantes, ultimo_caracter


def recuento_fonemas(transcripcion_4):
    # Se contabilizan los fonemas que tiene la transcripción
    # Se entrega la lista ordenada
    # de ocurrencias de cada caso



    ene_a = (transcripcion_4.count("a")) + (transcripcion_4.count("A"))
    ene_b = transcripcion_4.count("b")
    ene_ch = transcripcion_4.count("∫")  # che
    ene_d = transcripcion_4.count("d")
    ene_e = (transcripcion_4.count("e")) + (transcripcion_4.count("E"))
    ene_f = transcripcion_4.count("f")
    ene_g = transcripcion_4.count("g")
    ene_i = (transcripcion_4.count("i")) + (transcripcion_4.count("I"))
    ene_x = transcripcion_4.count("x")
    ene_k = transcripcion_4.count("k")
    ene_l = transcripcion_4.count("l")
    ene_y = transcripcion_4.count("ç")
    ene_m = transcripcion_4.count("m")
    ene_n = transcripcion_4.count("n")
    ene_N = transcripcion_4.count("N")
    ene_ñ = transcripcion_4.count("ñ")
    ene_o = (transcripcion_4.count("o")) + (transcripcion_4.count("O"))
    ene_p = transcripcion_4.count("p")
    ene_r = transcripcion_4.count("ɾ")
    ene_rr = transcripcion_4.count("r")
    ene_R = transcripcion_4.count("R")
    ene_s = transcripcion_4.count("s")
    ene_t = transcripcion_4.count("t")
    ene_u = (transcripcion_4.count("u")) + (transcripcion_4.count("U"))
    ene_B = transcripcion_4.count("B")
    ene_D = transcripcion_4.count("D")
    ene_G = transcripcion_4.count("G")


# Se agrega contador de fonemas y archifonemas diferentes.
    contador_total_fonemas_diferentes = 0
    contador_total_archifonemas_diferentes = 0

    if ene_a > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_b > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_ch > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_d > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_e > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_f > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_g > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_i > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_x > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_k > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_l > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_y > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_m > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_n > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_ñ > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_N > 0:
        contador_total_archifonemas_diferentes = contador_total_archifonemas_diferentes + 1
    if ene_o > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_p > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_r > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_rr > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_R > 0:
        contador_total_archifonemas_diferentes = contador_total_archifonemas_diferentes + 1
    if ene_s > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_t > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_u > 0:
        contador_total_fonemas_diferentes = contador_total_fonemas_diferentes + 1
    if ene_B > 0:
        contador_total_archifonemas_diferentes = contador_total_archifonemas_diferentes + 1
    if ene_D > 0:
        contador_total_archifonemas_diferentes = contador_total_archifonemas_diferentes + 1

    print("Total de fonemas diferentes:")
    print(contador_total_fonemas_diferentes)
    print("Total de archifonemas diferentes:")
    print(contador_total_archifonemas_diferentes)



    frecuencia_fonemas = [("a", ene_a), ("b", ene_b), ("ch", ene_ch), ("d", ene_d), ("e", ene_e), ("f", ene_f),
                          ("g", ene_g), ("i", ene_i), ("x", ene_x), ("k", ene_k), ("l", ene_l), ("y", ene_y),
                          ("m", ene_m), ("n", ene_n), ("N", ene_N), ("ñ", ene_ñ), ("o", ene_o), ("p", ene_p),
                          ("r", ene_r), ("rr", ene_rr), ("R", ene_R), ("s", ene_s), ("t", ene_t), ("u", ene_u),
                          ("B", ene_B), ("D", ene_D), ("G", ene_G)]

    total_fonemas = (ene_a + ene_b + ene_ch + ene_d + ene_e + ene_f + ene_g +
                     ene_i + ene_x + ene_k + ene_l + ene_m + ene_n + ene_ñ + ene_N +
                     ene_y + ene_o + ene_p + ene_r + ene_rr + ene_s + ene_t + ene_u +
                     ene_B + ene_D + ene_G)



    frec_fonemas_dict = dict(frecuencia_fonemas)
    frec_fonemas_orden = sorted(frec_fonemas_dict.items(), key=operator.itemgetter(1), reverse=True)

    cantidad_fonemas_vocales = (ene_a + ene_e + ene_i + ene_o + ene_u)
    cantidad_consonantes = (total_fonemas - cantidad_fonemas_vocales)
    cantidad_vocales_anteriores = (ene_e + ene_i)
    cantidad_vocales_posteriores = (ene_o + ene_u)
    cantidad_vocales_cerradas = (ene_i + ene_u)
    cantidad_vocales_abiertas = (ene_a + ene_e + ene_o)
    cantidad_fonemas_nasales = (ene_m + ene_n + ene_ñ + ene_N)
    cantidad_fonemas_orales = (total_fonemas - cantidad_fonemas_nasales)
    cantidad_fonemas_fricativos_sordos = (ene_s + ene_f + ene_x)
    cantidad_fonemas_posteriores = (ene_x + ene_k + ene_g + ene_G)
    cantidad_fonemas_anteriores = (
            ene_s + ene_f + ene_N + ene_n + ene_l + ene_R + ene_r + ene_rr + ene_t + ene_d + ene_D)
    cantidad_fonemas_centrales = (ene_ch + ene_ñ + ene_y)
    cantidad_fonemas_consonantes_sonoras = (
            ene_b + ene_d + ene_g + ene_l + ene_ñ + ene_n + ene_m + ene_R + ene_r + ene_rr + ene_y)
    cantidad_fonemas_consonantes_sordas = (ene_p + ene_t + ene_k + cantidad_fonemas_fricativos_sordos + ene_ch)

    return frec_fonemas_orden, total_fonemas, cantidad_fonemas_vocales, cantidad_consonantes, \
           cantidad_vocales_anteriores, cantidad_vocales_posteriores, \
           cantidad_vocales_cerradas, cantidad_vocales_abiertas, \
           cantidad_fonemas_nasales, cantidad_fonemas_orales, cantidad_fonemas_fricativos_sordos, \
           cantidad_fonemas_posteriores, cantidad_fonemas_anteriores, cantidad_fonemas_centrales, \
           cantidad_fonemas_consonantes_sonoras, cantidad_fonemas_consonantes_sordas


def conversor_cv(transcripcion_4):
    cadena_cv = transcripcion_4.replace(" ", "")

    # sin creer
    # el dos para las sílaba con coda compleja
    conversionCV = [("uai", "0v0"), ("iai", "0v0"), ("iei", "0v0"), ("uau", "0v0"), ("iau", "0v0"), ("uei", "0v0"),
                    ("ui", "v0"), ("iu", "v0"), ("ai", "v0"), ("ei", "v0"), ("ei", "v0"), ("au", "v0"), ("eu", "v0"),
                    ("ia", "0v"), ("ie", "0v"), ("io", "0v"), ("oi", "v0"), ("ou", "v0"), ("ue", "0v"), ("uo", "0v"),
                    ("ua", "0v"),
                    ("uAi", "0v0"), ("iAi", "0v0"), ("iEi", "0v0"), ("uAu", "0v0"), ("iAu", "0v0"), ("uEi", "0v0"),
                    ("Ui", "v0"), ("Iu", "v0"), ("Ai", "v0"), ("Ei", "v0"), ("Ei", "v0"), ("Au", "v0"), ("Eu", "v0"),
                    ("iA", "0v"), ("iE", "0v"), ("iO", "0v"), ("Oi", "v0"), ("Ou", "v0"), ("uE", "0v"), ("uO", "0v"),
                    ("uA", "0v"),
                    ("A", "v"), ("E", "v"), ("I", "v"), ("O", "v"), ("U", "v"),
                    ("a", "v"), ("e", "v"), ("i", "v"), ("o", "v"), ("u", "v"),
                    ("vbstv", "vc2cv"),
                    ("vbsk", "vc2c"), ("vbssv", "vc2cv"),
                    ("tɾvNsb", "c1vc2b"),
                    ("tɾvNsd", "c1vc2d"), ("tɾvNsf", "c1vc2f"), ("tɾvNsg", "c1vc2g"), ("tɾvNsl", "c1vc2l"),
                    ("tɾvNsm", "c1vc2m"), ("tɾvNsn", "c1vc2n"), ("tɾvNsp", "c1vc2p"), ("tɾvNsk", "c1vc2k"),
                    ("vkskl", "vc2c1"), ("vkssv", "vc2cv"), ("kvNss", "cvc2c"),
                    #
                    ("vNkɾv", "vc2c1v"),
                    #
                    ("vGstɾv", "vc2c1v"),
                    ("vNstɾ", "vc2c1"), ("vNst", "vc2c"), ("vNsc", "vc2c"), ("vNspv", "vc2cv"),
                    ("Nstv", "c2cv"), ("Nspv", "c2cv"),
                    ("Bst", "c2c"), ("Bssv", "c2cv"),
                    ("Gstɾ", "c2c1"), ("kvNss", "cvc2c"), ("vGskv", "vc2cv"), ("vGsklv", "vc2c1v"),
                    ("Gspl", "c2c1"), ("Gspɾ", "c2c1"), ("Gsp", "c2c"), ("Gss", "c2c"), ("Gstv", "c2cv"),
                    ("Gsgv", "c2cv"),
                    ("bɾ", "c1"), ("bl", "c1"), ("kɾ", "c1"), ("kl", "c1"), ("dɾ", "c1"), ("fɾ", "c1"), ("fl", "c1"),
                    ("gɾ", "c1"), ("gl", "c1"), ("pl", "c1"), ("pɾ", "c1"), ("tl", "c1"), ("tɾ", "c1"), ("b", "c"),
                    ("d", "c"), ("f", "c"), ("g", "c"), ("x", "c"), ("k", "c"), ("l", "c"), ("m", "c"), ("n", "c"),
                    ("ñ", "c"), ("p", "c"), ("ɾ", "c"), ("s", "c"), ("∫", "c"), ("t", "c"), ("ç", "c"), ("I", "v"),
                    ("U", "v"), ("r", "c"), ("R", "c"), ("N", "c"), ("B", "c"), ("D", "c"), ("G", "c"), ("ç", "c"), ]

    texto_convertido_cv = cadena_cv

    for remplazoCV in conversionCV:
        texto_convertido_cv = texto_convertido_cv.replace(remplazoCV[0], remplazoCV[1])

    return texto_convertido_cv


def analizador_silabico(texto_convertido_cv):
    texto_convertido_cv_2 = texto_convertido_cv.replace("|", "9").replace("‖", "9")

    texto_convertido_cv_2_separado = texto_convertido_cv_2.split("9")

    n_de_v = texto_convertido_cv_2.count("v")

    #    print ( "Texto convertido a CV..." )
    #    print ( texto_convertido_cv )
    #    print ( "=============================================" )

    #    print ( "texto cv con '9' final en cada grupo: " )
    #    print ( texto_convertido_cv_2 )
    #    print ( "=============================================" )

    #    print ( "Texto de los grupos separados por '9'")

    #    print ( texto_convertido_cv_2_separado )
    #    print ( "=============================================" )

    ene_tipo_c10v0c2 = 0  # triauns  7   Nueva:  1
    ene_tipo_c10vc2 = 0  # trians    6   Nueva:  2
    ene_tipo_c1v0c2 = 0  # trains    6   Nueva:  3
    ene_tipo_c1vc2 = 0  # 26 trans   5   Nueva:  4
    ene_tipo_c0v0c = 0  # 27 tieis   5   Nueva:  5
    ene_tipo_cv0c2 = 0  # 23 tains  5   Nueva:  6
    ene_tipo_c0vc2 = 0  # 24 tians  5   Nueva:  7
    ene_tipo_c10vc = 0  # 17 trian  5   Nueva:  8
    ene_tipo_c1v0c = 0  # 18 train  5   Nueva:  9
    ene_tipo_c10v = 0  # 14 tria    4   Nueva:  10
    ene_tipo_c1v0 = 0  # 15 trai    4   Nueva:  11
    ene_tipo_c1vc = 0  # 16 tras    4   Nueva:  12
    ene_tipo_c0v0 = 0  # 19 tiau    4   Nueva:  13
    ene_tipo_0vc2 = 0  # 21 ians    4   Nueva:  14
    ene_tipo_0v0c = 0  # iaun    4   Nueva:  15
    ene_tipo_v0c2 = 0  # 22 ains    4   Nueva:  16
    ene_tipo_cvc2 = 0  # 25 tans    4   Nueva:  17
    ene_tipo_c0vc = 0  # 8 tian     4   Nueva:  18
    ene_tipo_cv0c = 0  # 9 tain     4   Nueva:  19
    ene_tipo_0vc = 0  # 11 ial      3   Nueva:  21
    ene_tipo_v0c = 0  # 12 ail      3   Nueva:  21
    ene_tipo_0v0 = 0  # no consid    3   Nueva:  22
    ene_tipo_c1v = 0  # 13 tra      3   Nueva:  23
    ene_tipo_vc2 = 0  # 20 ans      3   Nueva:  24
    ene_tipo_c0v = 0  # 5 tia       3   Nueva:  25
    ene_tipo_cv0 = 0  # 6 tai       3   Nueva:  26
    ene_tipo_cvc = 0  # 7 tas       3   Nueva:  27
    ene_tipo_v0 = 0  # 2 ai         2   Nueva:  28
    ene_tipo_0v = 0  # 3 ia         2   Nueva:  29
    ene_tipo_cv = 0  # 4 ta         2   Nueva:  30
    ene_tipo_vc = 0  # 10 al        2   Nueva:  31
    ene_tipo_v = 0  # 1 a           1   Nueva:  32

    for grupo in texto_convertido_cv_2_separado:

        if grupo != "":
            grupo += "9"  # agrega "9" para finalizar el grupo
            largo_grupo = len(grupo)
            n_v_grupo = grupo.count("v")  # número de vocales silábicas

            for ene_de_la_silaba in range(n_v_grupo):
                if grupo.startswith("c10v0c2"):
                    ene_tipo_c10v0c2 = ene_tipo_c10v0c2 + 1
                    grupo = grupo[7:largo_grupo]
                    # caso 1
                elif grupo.startswith("c10vc2"):
                    ene_tipo_c10vc2 = ene_tipo_c10vc2 + 1
                    grupo = grupo[6:largo_grupo]
                    # caso 2
                elif grupo.startswith("c1v0c2"):
                    ene_tipo_c1v0c2 = ene_tipo_c1v0c2 + 1
                    grupo = grupo[6:largo_grupo]
                    # caso 3
                elif grupo.startswith("c1vc2"):
                    ene_tipo_c1vc2 = ene_tipo_c1vc2 + 1
                    grupo = grupo[5:largo_grupo]
                    # caso 4
                elif grupo.startswith("c0v0cc"):
                    ene_tipo_c0v0c = ene_tipo_c0v0c + 1
                    grupo = grupo[5:largo_grupo]
                    # caso 5
                elif grupo.startswith("cv0c2"):
                    ene_tipo_cv0c2 = ene_tipo_cv0c2 = + 1
                    grupo = grupo[5:largo_grupo]
                    # caso 6
                elif grupo.startswith("c0vc2"):
                    ene_tipo_c0vc2 = ene_tipo_c0vc2 = + 1
                    grupo = grupo[5:largo_grupo]
                    # caso 7
                elif grupo.startswith("c10vcc"):
                    ene_tipo_c10vc = ene_tipo_c10vc + 1
                    grupo = grupo[5:largo_grupo]
                    # caso 8
                elif grupo.startswith("c1v0cc"):
                    ene_tipo_c1v0c = ene_tipo_c1v0c + 1
                    grupo = grupo[5:largo_grupo]
                    # caso 9
                elif grupo.startswith("c10vv") or grupo.startswith("c10vcv") or grupo.startswith("c10vc1") or \
                        grupo.startswith("c10vc0"):
                    ene_tipo_c10v = ene_tipo_c10v + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 10
                elif grupo.startswith("c1v0v") or grupo.startswith("c1v0cv") or grupo.startswith("c1v0c1") or \
                        grupo.startswith("c1v0c0"):
                    ene_tipo_c1v0 = ene_tipo_c1v0 + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 11
                elif grupo.startswith("c1vcc"):
                    ene_tipo_c1vc = ene_tipo_c1vc + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 12
                elif grupo.startswith("c0v0cv") or grupo.startswith("c0v0c0") or grupo.startswith("c0v0c1"):
                    ene_tipo_c0v0 = ene_tipo_c0v0 + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 13
                elif grupo.startswith("0vc2"):
                    ene_tipo_0vc2 = ene_tipo_0vc2 + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 14
                elif grupo.startswith("0v0cc"):
                    ene_tipo_0v0c = ene_tipo_0v0c + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 15
                elif grupo.startswith("v0c2"):
                    ene_tipo_v0c2 = ene_tipo_v0c2 + 1
                    # caso 16
                elif grupo.startswith("cvc2"):
                    ene_tipo_cvc2 = ene_tipo_cvc2 = + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 17
                elif grupo.startswith("c0vcc"):
                    ene_tipo_c0vc = ene_tipo_c0vc + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 18
                elif grupo.startswith("cv0cc"):
                    ene_tipo_cv0c = ene_tipo_cv0c + 1
                    grupo = grupo[4:largo_grupo]
                    # caso 19
                elif grupo.startswith("0vcc"):
                    ene_tipo_0vc = ene_tipo_0vc + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 20
                elif grupo.startswith("v0cc"):
                    ene_tipo_v0c = ene_tipo_v0c + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 21
                elif grupo.startswith("0v0cv") or grupo.startswith("0v0c1") or grupo.startswith(
                        "0v0c0") or grupo.startswith("0v0vv"):
                    ene_tipo_0v0 = ene_tipo_0v0 + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 22
                #     ene_tipo_0vc =
                elif grupo.startswith("c1vv") or grupo.startswith("c1vc1") or grupo.startswith("c1vc0") \
                        or grupo.startswith("c1vcv"):
                    ene_tipo_c1v = ene_tipo_c1v + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 23
                elif grupo.startswith("vc2"):
                    ene_tipo_vc2 = ene_tipo_vc2 + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 24
                elif grupo.startswith("c0vv") or grupo.startswith("c0vcv") or grupo.startswith("c0vc0") or \
                        grupo.startswith("c0vc1") or grupo.startswith("c0v0v"):
                    ene_tipo_c0v = ene_tipo_c0v + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 25
                elif grupo.startswith("cv0v") or grupo.startswith("cv0cv") or grupo.startswith("cv0c1") \
                        or grupo.startswith("cv0c0"):
                    ene_tipo_cv0 = ene_tipo_cv0 + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 26
                elif grupo.startswith("cvcc"):
                    ene_tipo_cvc = ene_tipo_cvc + 1
                    grupo = grupo[3:largo_grupo]
                    # caso 27
                elif grupo.startswith("v0v0") or grupo.startswith("v0cv") or grupo.startswith(
                        "v0c1") or grupo.startswith("v0c0"):
                    ene_tipo_v0 = ene_tipo_v0 + 1
                    grupo = grupo[2:largo_grupo]
                    # caso 28 revisar condiciones
                elif grupo.startswith("0vv") or grupo.startswith("0vcv") or grupo.startswith("0vc1") \
                        or grupo.startswith("0vc0"):
                    ene_tipo_0v = ene_tipo_0v + 1
                    grupo = grupo[2:largo_grupo]
                    # caso 29
                elif grupo.startswith("cvv") or grupo.startswith("cvcv") or grupo.startswith("cvc1") or \
                        grupo.startswith("cvc0"):
                    ene_tipo_cv = ene_tipo_cv + 1
                    grupo = grupo[2:largo_grupo]
                    # caso 30
                elif grupo.startswith("vcc"):
                    ene_tipo_vc = ene_tipo_vc + 1
                    grupo = grupo[2:largo_grupo]
                    # caso 31
                elif grupo.startswith("vv") or grupo.startswith("vcv") or grupo.startswith("vc0") or \
                        grupo.startswith("vc1") or grupo.startswith("v0v"):
                    ene_tipo_v = ene_tipo_v + 1
                    grupo = grupo[1:largo_grupo]
                    # caso 32
                elif grupo == "c10v0c29":
                    ene_tipo_c10v0c2 = ene_tipo_c10v0c2 + 1
                elif grupo == "c10vc29":
                    ene_tipo_c10vc2 = ene_tipo_c10vc2 + 1
                elif grupo == "c1v0c29":
                    ene_tipo_c1v0c2 = ene_tipo_c1v0c2 + 1
                elif grupo == "c1vc29":
                    ene_tipo_c1vc2 = ene_tipo_c1vc2 + 1
                elif grupo == "c0v0c9":
                    ene_tipo_c0v0c = ene_tipo_c0v0c + 1
                elif grupo == "cv0c29":
                    ene_tipo_cv0c2 = ene_tipo_cv0c2 + 1
                elif grupo == "c0vc29":
                    ene_tipo_c0vc2 = ene_tipo_c0vc2 + 1
                elif grupo == "c10vc9":
                    ene_tipo_c10vc = ene_tipo_c10vc + 1
                elif grupo == "c1v0c9":
                    ene_tipo_c1v0c = ene_tipo_c1v0c + 1
                elif grupo == "c10v9":
                    ene_tipo_c10v = ene_tipo_c10v + 1
                elif grupo == "c1v09":
                    ene_tipo_c1v0 = ene_tipo_c1v0 + 1
                elif grupo == "c1vc9":
                    ene_tipo_c1vc = ene_tipo_c1vc + 1
                elif grupo == "c0v09":
                    ene_tipo_c0v0 = ene_tipo_c0v0 + 1
                elif grupo == "0vc29":
                    ene_tipo_0vc2 = ene_tipo_0vc2 + 1
                elif grupo == "v0c29":
                    ene_tipo_v0c2 = ene_tipo_v0c2 + 1
                elif grupo == "cvc29":
                    ene_tipo_cvc2 = ene_tipo_cvc2 + 1
                elif grupo == "c0vc9":
                    ene_tipo_c0vc = ene_tipo_c0vc + 1
                elif grupo == "cv0c9":
                    ene_tipo_cv0c = ene_tipo_cv0c + 1
                elif grupo == "0vc9":
                    ene_tipo_0vc = ene_tipo_0vc + 1
                elif grupo == "v0c9":
                    ene_tipo_v0c = ene_tipo_v0c + 1
                elif grupo == "c1v9":
                    ene_tipo_c1v = ene_tipo_c1v + 1
                elif grupo == "vc29":
                    ene_tipo_vc2 = ene_tipo_vc2 + 1
                elif grupo == "c0v9":
                    ene_tipo_c0v = ene_tipo_c0v + 1
                elif grupo == "cv09":
                    ene_tipo_cv0 = ene_tipo_cv0 + 1
                elif grupo == "cvc9":
                    ene_tipo_cvc = ene_tipo_cvc + 1
                elif grupo == "v09":
                    ene_tipo_v0 = ene_tipo_v0 + 1
                elif grupo == "0v9":
                    ene_tipo_0v = ene_tipo_0v + 1
                elif grupo == "cv9":
                    ene_tipo_cv = ene_tipo_cv + 1
                elif grupo == "vc9":
                    ene_tipo_vc = ene_tipo_vc + 1
                elif grupo == "v9":
                    ene_tipo_v = ene_tipo_v + 1
                else:
                    print("caso no considerado!!!")

    sumatoria_todo_tipo = ene_tipo_c10v0c2 + ene_tipo_c10vc2 + ene_tipo_c1v0c2 + ene_tipo_c1vc2 + ene_tipo_c0v0c + \
                          ene_tipo_cv0c2 + ene_tipo_c0vc2 + ene_tipo_c10vc + ene_tipo_c1v0c + ene_tipo_c10v + \
                          ene_tipo_c1v0 + ene_tipo_c1vc + ene_tipo_c0v0 + ene_tipo_0vc2 + ene_tipo_0v0c + \
                          ene_tipo_v0c2 + ene_tipo_cvc2 + ene_tipo_c0vc + ene_tipo_cv0c + ene_tipo_0vc + \
                          ene_tipo_v0c + ene_tipo_0v0 + ene_tipo_c1v + ene_tipo_vc2 + ene_tipo_c0v + ene_tipo_cv0 + \
                          ene_tipo_cvc + ene_tipo_v0 + ene_tipo_0v + ene_tipo_cv + ene_tipo_vc + ene_tipo_v

    sumatoria_silabas_abiertas = ene_tipo_c10v + ene_tipo_c1v0 + ene_tipo_c0v0 + ene_tipo_0v0 + ene_tipo_c0v + \
                                 ene_tipo_cv0 + ene_tipo_v0 + ene_tipo_0v + ene_tipo_0v + ene_tipo_cv + ene_tipo_v

    sumatoria_diptongos = ene_tipo_c10vc2 + ene_tipo_c1v0c2 + ene_tipo_cv0c2 + ene_tipo_c0vc2 + \
                          ene_tipo_c10vc + ene_tipo_c1v0c + ene_tipo_c10v + ene_tipo_c1v0 + ene_tipo_0vc2 + \
                          ene_tipo_v0c2 + ene_tipo_c0vc + ene_tipo_cv0c + ene_tipo_0vc + ene_tipo_v0c + ene_tipo_c0v + \
                          ene_tipo_cv0 + ene_tipo_v0 + ene_tipo_0v

    sumatoria_triptongos = ene_tipo_c10v0c2 + ene_tipo_c0v0c + ene_tipo_c0v0 + ene_tipo_0v0c + ene_tipo_0v0

    sumatoria_dip_trip_tongos = sumatoria_diptongos + sumatoria_triptongos

    sumatoria_dip_crecientes = ene_tipo_c10vc2 + ene_tipo_c0vc2 + ene_tipo_c10vc + ene_tipo_c10v + ene_tipo_0vc2 \
                               + ene_tipo_c0vc + ene_tipo_0vc + ene_tipo_c0v + ene_tipo_0v

    sumatoria_dip_decrecientes = ene_tipo_c1v0c2 + ene_tipo_cv0c2 + ene_tipo_c1v0c + ene_tipo_c1v0 + ene_tipo_v0c2 + \
                                 ene_tipo_cv0c + ene_tipo_v0c + ene_tipo_cv0 + ene_tipo_v0

    sumatoria_inicio_consonante = ene_tipo_c10v0c2 + ene_tipo_c10vc2 + ene_tipo_c1v0c2 + ene_tipo_c1vc2 + \
                                  ene_tipo_c0v0c + ene_tipo_cv0c2 + ene_tipo_c0vc2 + ene_tipo_c10vc + ene_tipo_c1v0c + \
                                  ene_tipo_c10v + ene_tipo_c1v0 + ene_tipo_c1vc + ene_tipo_c0v0 + ene_tipo_cvc2 + \
                                  ene_tipo_c0vc + ene_tipo_cv0c + ene_tipo_c1v + ene_tipo_c0v + ene_tipo_cv0 + \
                                  ene_tipo_cvc + ene_tipo_cv

    sumatoria_inicio_cons_simple = ene_tipo_c0v0c + ene_tipo_cv0c2 + ene_tipo_c0vc2 + ene_tipo_c0v0 + ene_tipo_cvc2 + \
                                   ene_tipo_c0vc + ene_tipo_cv0c + ene_tipo_c0v + ene_tipo_cv0 + ene_tipo_cvc + \
                                   ene_tipo_cv

    sumatoria_inicio_cons_comple = ene_tipo_c10v0c2 + ene_tipo_c10vc2 + ene_tipo_c1v0c2 + ene_tipo_c1vc2 + ene_tipo_c10vc + ene_tipo_c1v0c + \
                                   ene_tipo_c10v + ene_tipo_c1v0 + ene_tipo_c1vc + ene_tipo_c1v

    sumatoria_silabas_cerradas = sumatoria_todo_tipo - sumatoria_silabas_abiertas

    sumatoria_sin_dip_trip_tongo = sumatoria_todo_tipo - sumatoria_dip_trip_tongos

    frecuencias_tipos_silabas = [("cCjvjCc", ene_tipo_c10v0c2), ("cCjvCc", ene_tipo_c10vc2),
                                 ("cCvjCc", ene_tipo_c1v0c2), ("cCvCc", ene_tipo_c1vc2), ("cjvjc", ene_tipo_c0v0c),
                                 ("cvjCc", ene_tipo_cv0c2), ("cjvCc", ene_tipo_c0vc2), ("cCjvc", ene_tipo_c10vc),
                                 ("cCvjc", ene_tipo_c1v0c), ("cCjv", ene_tipo_c10v), ("cCvj", ene_tipo_c1v0),
                                 ("cCvc", ene_tipo_c1vc), ("cjvj", ene_tipo_c0v0), ("jvCc", ene_tipo_0vc2),
                                 ("jvjc", ene_tipo_0v0c), ("vjCc", ene_tipo_v0c2), ("cvCc", ene_tipo_cvc2),
                                 ("cjvc", ene_tipo_c0vc), ("cvjc", ene_tipo_cv0c), ("jvc", ene_tipo_0vc),
                                 ("vjc", ene_tipo_v0c), ("jvj", ene_tipo_0v0), ("cCv", ene_tipo_c1v),
                                 ("vCc", ene_tipo_vc2), ("cjv", ene_tipo_c0v), ("cvj", ene_tipo_cv0),
                                 ("cvc", ene_tipo_cvc), ("vj", ene_tipo_v0), ("jv", ene_tipo_0v),
                                 ("cv", ene_tipo_cv), ("vc", ene_tipo_vc), ("v", ene_tipo_v)]

    frec_silabas_dict = dict(frecuencias_tipos_silabas)

    frec_silabas_orden = sorted(frec_silabas_dict.items(), key=operator.itemgetter(1), reverse=True)

    if sumatoria_todo_tipo == n_de_v:
        print("Coinciden los recuentos de Nº de sílabas por dos vías")
    else:
        print("No coinciden los recuentos por las dos vías")

    return ene_tipo_c10v0c2, ene_tipo_c10vc2, ene_tipo_c1v0c2, ene_tipo_c1vc2, ene_tipo_c0v0c, ene_tipo_cv0c2, \
           ene_tipo_c0vc2, ene_tipo_c10vc, ene_tipo_c1v0c, ene_tipo_c10v, ene_tipo_c1v0, ene_tipo_c1vc, \
           ene_tipo_c0v0, ene_tipo_0vc2, ene_tipo_0v0c, ene_tipo_v0c2, ene_tipo_cvc2, ene_tipo_c0vc, \
           ene_tipo_cv0c, ene_tipo_0vc, ene_tipo_v0c, ene_tipo_0v0, ene_tipo_c1v, ene_tipo_vc2, ene_tipo_c0v, \
           ene_tipo_cv0, ene_tipo_cvc, ene_tipo_v0, ene_tipo_0v, ene_tipo_cv, ene_tipo_vc, ene_tipo_v, \
           sumatoria_todo_tipo, n_de_v, frec_silabas_orden, frecuencias_tipos_silabas, \
           sumatoria_silabas_abiertas, sumatoria_silabas_cerradas, \
           sumatoria_diptongos, sumatoria_triptongos, sumatoria_dip_crecientes, sumatoria_dip_decrecientes, \
           sumatoria_dip_trip_tongos, sumatoria_sin_dip_trip_tongo, \
           sumatoria_inicio_consonante, sumatoria_inicio_cons_simple, sumatoria_inicio_cons_comple

def graficos_fonemas(frec_fonemas_orden, total_fonemas, cantidad_fonemas_vocales, cantidad_consonantes,
                     cantidad_vocales_anteriores, cantidad_vocales_posteriores, cantidad_vocales_cerradas,
                     cantidad_vocales_abiertas, cantidad_fonemas_nasales, cantidad_fonemas_orales,
                     cantidad_fonemas_fricativos_sordos, cantidad_fonemas_posteriores,
                     cantidad_fonemas_anteriores, cantidad_fonemas_centrales,
                     cantidad_fonemas_consonantes_sonoras, cantidad_fonemas_consonantes_sordas):
    lista_fon_repres = []
    lista_fon_valore = []

    for fonema in frec_fonemas_orden:
        lista_fon_repres.append(fonema[0])
        lista_fon_valore.append(fonema[1])

    plt.plot(lista_fon_valore, linestyle=":", marker="o", color="blue", markersize=4, drawstyle="steps")
    plt.grid()
    plt.title("Frecuencia ordenada de fonemas, n = " + str(total_fonemas))
    plt.ylabel("Ocurrencias")
    plt.xlabel("Fonemas")
    eje_fonemas = range(len(lista_fon_repres))
    plt.xticks(eje_fonemas, lista_fon_repres)
    plt.ylim(0)
    plt.show()

    # Vocales vs. consonantes
    categorias = ['Vocales', 'Consonantes']
    valores = [cantidad_fonemas_vocales, cantidad_consonantes]
    ene = (cantidad_consonantes + cantidad_fonemas_vocales)
    plt.bar(categorias, valores, color=['darksalmon', 'olive'])
    plt.ylabel("Ocurrencias")
    plt.xlabel("Tipo de fonema")
    plt.title("Vocales y consonantes, n = " + str(ene))
    plt.show()

    categorias = ['Vocales', 'Consonantes']
    valores = [cantidad_fonemas_vocales, cantidad_consonantes]
    ene = (cantidad_consonantes + cantidad_fonemas_vocales)

    plt.pie(valores, labels=categorias, autopct='%1.1f%%')
    plt.title("Vocales y consonantes, n = " + str(total_fonemas))
    plt.show()

    # vocales anteriores vs vocales posteriores
    categorias = ['palatales', 'velares']
    valores = [cantidad_vocales_anteriores, cantidad_vocales_posteriores]
    ene = (cantidad_vocales_anteriores + cantidad_vocales_posteriores)
    plt.bar(categorias, valores, color=['gold', 'slateblue'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Tipo de vocal')
    plt.title("Vocales palatales y velares, n = " + str(ene))
    plt.show()

    # vocales abiertas vs cerradas
    categorias = ['abiertas', 'cerradas']
    valores = [cantidad_vocales_abiertas, cantidad_vocales_cerradas]
    ene = (cantidad_vocales_abiertas + cantidad_vocales_cerradas)
    plt.bar(categorias, valores, color=['mistyrose', 'teal'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Tipo de vocal')
    plt.title("Vocales abiertas y cerradas, n = " + str(ene))

    plt.show()

    # nasales vs. orales
    categorias = ['nasales', 'orales']
    valores = [cantidad_fonemas_nasales, cantidad_fonemas_orales]
    ene = (cantidad_fonemas_nasales + cantidad_fonemas_orales)
    plt.bar(categorias, valores, color=['goldenrod', 'rosybrown'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Tipo de resonancia')
    plt.title("Consonantes nasales y orales, n = " + str(ene))

    plt.show()

    # por punto de articulacion
    categorias = ['anteriores', 'centrales', 'velares']
    valores = [cantidad_fonemas_anteriores, cantidad_fonemas_centrales, cantidad_fonemas_posteriores]
    ene = (cantidad_fonemas_anteriores + cantidad_fonemas_centrales + cantidad_fonemas_posteriores)
    plt.bar(categorias, valores, color=['tomato', 'goldenrod', 'blueviolet'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Zona')
    plt.title("Zonas articulatorias consonánticas, n = " + str(ene))

    plt.show()

    # acción de las cuerdas vocales
    categorias = ['sonoras', 'sordas']
    valores = [cantidad_fonemas_consonantes_sonoras, cantidad_fonemas_consonantes_sordas]
    ene = (cantidad_fonemas_consonantes_sonoras + cantidad_fonemas_consonantes_sordas)
    plt.bar(categorias, valores, color=['darksalmon', 'dodgerblue'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Zona')
    plt.title("Acción de las cuerdas vocales, n = " + str(ene))

    plt.show()


def graficos_silabas(frecuencia_silabas_orden, sumatoria_todo_tipo, n_de_v, frec_silabas_orden,
                     frecuencias_tipos_silabas, sumatoria_silabas_abiertas, sumatoria_silabas_cerradas,
                     sumatoria_diptongos, sumatoria_triptongos, sumatoria_dip_crecientes, sumatoria_dip_decrecientes,
                     sumatoria_dip_trip_tongos, sumatoria_sin_dip_trip_tongo, sumatoria_inicio_consonante,
                     sumatoria_inicio_cons_simple, sumatoria_inicio_cons_comple):
    # Primer gráfico
    print("Primer gráfico: 11 tipos más frecuentes")
    print("Sobre un ene de", str(sumatoria_todo_tipo), "sílabas")

    lista_sil_repres_2 = []
    lista_sil_valore_2 = []

    for tipo_silaba in frecuencia_silabas_orden[0:11]:
        lista_sil_repres_2.append(tipo_silaba[0])
        lista_sil_valore_2.append(tipo_silaba[1])

    plt.plot(lista_sil_valore_2, linestyle=":", marker="o", color="red", markersize=4, drawstyle="steps")
    plt.grid()
    plt.title("11 Tipos silábicos más frecuentes, ene = " + str(sumatoria_todo_tipo))
    plt.ylabel("Ocurrencias")
    #  plt.xlabel ( "Tipos" )
    plt.ylim(0)
    eje_tipos_silabas = range(len(lista_sil_repres_2))
    plt.xticks(eje_tipos_silabas, lista_sil_repres_2, rotation=90, fontsize=8)
    plt.show()

    # segundo gráfico:
    # otros 10

    lista_sil_repres_2 = []
    lista_sil_valore_2 = []

    for tipo_silaba in frecuencia_silabas_orden[11:22]:
        lista_sil_repres_2.append(tipo_silaba[0])
        lista_sil_valore_2.append(tipo_silaba[1])

    plt.plot(lista_sil_valore_2, linestyle=":", marker="o", color="red", markersize=4, drawstyle="steps")
    plt.grid()
    plt.title("11 tipos silábicos segundas frecuencias")
    plt.ylabel("Ocurrencias")
    #   plt.xlabel ( "Tipos" )
    plt.ylim(0)
    eje_tipos_silabas = range(len(lista_sil_repres_2))
    plt.xticks(eje_tipos_silabas, lista_sil_repres_2, rotation=90, fontsize=8)
    plt.show()

    lista_sil_repres_2 = []
    lista_sil_valore_2 = []

    for tipo_silaba in frecuencia_silabas_orden[22:32]:
        lista_sil_repres_2.append(tipo_silaba[0])
        lista_sil_valore_2.append(tipo_silaba[1])

    plt.plot(lista_sil_valore_2, linestyle=":", marker="o", color="red", markersize=4, drawstyle="steps")
    plt.grid()
    plt.title("10 tipos silábicos terceras frecuencias")
    plt.ylabel("Ocurrencias")
    #   plt.xlabel ( "Tipos" )
    plt.ylim(0)
    eje_tipos_silabas = range(len(lista_sil_repres_2))
    plt.xticks(eje_tipos_silabas, lista_sil_repres_2, rotation=90, fontsize=8)
    plt.show()

    # tercer gráfico:
    # Todas las sílabas

    lista_sil_repres_2 = []
    lista_sil_valore_2 = []

    for tipo_silaba in frecuencia_silabas_orden[0:33]:
        lista_sil_repres_2.append(tipo_silaba[0])
        lista_sil_valore_2.append(tipo_silaba[1])
    plt.figure(figsize=(10, 8))
    plt.plot(lista_sil_valore_2, linestyle=":", marker="o", color="red", markersize=4, drawstyle="steps")
    plt.grid()
    plt.title("Tipos silábicos posibles")
    plt.ylabel("Ocurrencias")
    plt.xlabel("Tipos")
    plt.ylim(0)
    eje_tipos_silabas = range(len(lista_sil_repres_2))
    plt.xticks(eje_tipos_silabas, lista_sil_repres_2, rotation=90)
    plt.show()

    # Cuarto (A) gráfico:
    # Todas las sílabas con presencia

    lista_sil_repres_2 = []
    lista_sil_valore_2 = []

    for tipo_silaba in frecuencia_silabas_orden:
        if tipo_silaba[1] > 0:
            lista_sil_repres_2.append(tipo_silaba[0])
            lista_sil_valore_2.append(tipo_silaba[1])

    plt.plot(lista_sil_valore_2, linestyle=":", marker="o", color="red", markersize=4, drawstyle="steps")
    plt.grid()
    plt.title("Tipos silábicos presentes")
    plt.ylabel("Ocurrencias")
    #    plt.xlabel ( "Tipos" )
    plt.ylim(0)
    eje_tipos_silabas = range(len(lista_sil_repres_2))
    plt.xticks(eje_tipos_silabas, lista_sil_repres_2, rotation=90, fontsize=8)
    plt.show()
    print(frecuencia_silabas_orden)

    # cuarto gráfico:
    # torta

    lista_sil_repres_2 = []
    lista_sil_valore_2 = []

    for tipo_silaba in frecuencia_silabas_orden[0:33]:
        lista_sil_repres_2.append(tipo_silaba[0])
        lista_sil_valore_2.append(tipo_silaba[1])

    plt.pie(lista_sil_valore_2, labels=lista_sil_repres_2, autopct='%1.1f%%')
    plt.title("Tipos silábicos posibles")

    plt.show()

    # Quinto gráfico:
    # torta, los 7 primeros

    lista_sil_repres_2 = []
    lista_sil_valore_2 = []

    for tipo_silaba in frecuencia_silabas_orden[0:7]:
        lista_sil_repres_2.append(tipo_silaba[0])
        lista_sil_valore_2.append(tipo_silaba[1])

    plt.pie(lista_sil_valore_2, labels=lista_sil_repres_2, autopct='%1.1f%%')
    plt.title("Los 7 tipos silábicos presentes de mayor presencia")

    plt.show()

    # Sílabas trabadas vs. abiertas
    # sumatoria_silabas_abiertas, sumatoria_silabas_cerradas
    categorias = ["Sílabas libres", "Sílabas trabadas"]
    datos = [sumatoria_silabas_abiertas, sumatoria_silabas_cerradas]
    plt.bar(categorias, datos, color=['gold', 'slateblue'])
    plt.title("Sílabas libres vs. sílabas trabadas")
    plt.show()

    plt.pie(datos, labels=categorias, autopct='%1.1f%%')
    plt.title("Sílabas libres vs. trabadas")
    plt.show()

    categorias = ["Con sec. tauto.", "Sin sec. tauto."]
    datos = [sumatoria_dip_trip_tongos, sumatoria_sin_dip_trip_tongo]
    plt.pie(datos, labels=categorias, autopct='%1.1f%%')
    plt.title("Con secuencia vocálica tautosilábica. vs. sin")
    plt.show()

    categorias = ["Con diptongo", "Con triptongo", "Sin sec. tautosíl."]
    datos = [sumatoria_diptongos, sumatoria_triptongos, sumatoria_sin_dip_trip_tongo]
    plt.pie(datos, labels=categorias, autopct='%1.1f%%')
    plt.title("Diptongos, triptongos y sílabas sin dip-trip.")
    plt.show()

    categorias = ["Con diptongo", "Con triptongo"]
    datos = [sumatoria_diptongos, sumatoria_triptongos]
    plt.pie(datos, labels=categorias, autopct='%1.1f%%')
    plt.title("Diptongos, triptongos")
    plt.show()

    categorias = ["Crecientes", "Decrecientes"]
    datos = [sumatoria_dip_crecientes, sumatoria_dip_decrecientes]
    plt.pie(datos, labels=categorias, autopct='%1.1f%%')
    plt.title("Tipos de diptongos")
    plt.show()

    sumatoria_inicio_vocal = sumatoria_todo_tipo - sumatoria_inicio_consonante
    categorias = ["Inicio consonante", "Inicio vocal"]
    datos = [sumatoria_inicio_consonante, sumatoria_inicio_vocal]
    plt.pie(datos, labels=categorias, autopct='%1.1f%%')
    plt.title("Elemento de inicio silábico")
    plt.show()

    categorias = ["Grupo consonántico", "Consonante simple"]
    datos = [sumatoria_inicio_cons_comple, sumatoria_inicio_cons_simple]
    plt.pie(datos, labels=categorias, autopct='%1.1f%%')
    plt.title("Tipo de inicio consonántico")
    plt.show()


def graficos_palabras(total_palabras, contador_atonas, contador_tonicas, contador_bisilabas_atonas,
                      contador_atonas_monosilabas, \
                      contador_tonicas_monosilabas, contador_agudas, contador_graves, contador_esdrujulas,
                      contador_sobresdrujulas):
    datos_ton_aton = [contador_atonas, contador_tonicas]
    plt.pie(datos_ton_aton)
    plt.title("Proporción de tónicas y átonas,  n = " + str(total_palabras))
    plt.show()

    datos_esdruj_grav_agud = [contador_esdrujulas, contador_graves, contador_agudas]
    plt.pie(datos_esdruj_grav_agud)
    plt.title("Proporción de esdrújulas, graves y agudas, n = " + str(
        contador_agudas + contador_esdrujulas + contador_graves))
    plt.show()

    categorias = ['Tónicas', 'átonas']
    valores = [contador_tonicas, contador_atonas]
    ene = (contador_tonicas + contador_atonas)
    plt.bar(categorias, valores, color=['goldenrod', 'rosybrown'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Tipo de palabra')
    plt.title("Cantidad de palabras tónicas y átonas, n = " + str(ene))
    plt.show()

    categorias = ['Sobresdrújulas', 'Esdrújulas', 'Graves', 'Agudas']
    valores = [contador_sobresdrujulas, contador_esdrujulas, contador_graves, contador_agudas]
    ene = (contador_sobresdrujulas + contador_esdrujulas + contador_graves + contador_agudas)
    plt.bar(categorias, valores, color=['orange', 'goldenrod', 'darkseagreen', 'yellowgreen'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Tipo de palabra')
    plt.title("Cantidad de palabras por tipo, n = " + str(ene))
    plt.show()

    # todos los tipos

    categorias = ['M. át.', 'M. tón.', 'B. át.', 'S.esdrúj.', 'Esdrúj.', 'Graves', 'Agudas']
    valores = [contador_atonas_monosilabas, contador_tonicas_monosilabas, contador_bisilabas_atonas,
               contador_sobresdrujulas, contador_esdrujulas, contador_graves, contador_agudas]
    ene = (
                contador_atonas_monosilabas + contador_tonicas_monosilabas + contador_bisilabas_atonas + contador_sobresdrujulas + contador_esdrujulas + contador_graves + contador_agudas)
    plt.bar(categorias, valores,
            color=['lightcoral', 'indianred', 'chocolate', 'orange', 'goldenrod', 'darkseagreen', 'yellowgreen'])
    plt.ylabel("Ocurrencias")
    plt.xlabel('Tipo de palabra')
    plt.title("Cantidad de palabras por tipo, n = " + str(ene))
    plt.show()
